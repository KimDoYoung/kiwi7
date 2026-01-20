
import json
import sqlite3

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.core.config import config
from backend.core.logger import get_logger
from backend.domains.kdemon.k_demon import KDemon, now_ymdhms

# APIRouter 인스턴스 생성
router = APIRouter()
logger = get_logger(__name__)

class CommandBody(BaseModel):
    cmd: str  # 'start' | 'stop' | 'refresh'
    args: dict | None = None

def _conn():
    DB_PATH = config.DB_PATH
    return sqlite3.connect(DB_PATH, check_same_thread=False)

@router.post("/command")
async def send_command(body: CommandBody):
    cmd = body.cmd.lower()
    if cmd not in {"start", "stop", "refresh"}:
        raise HTTPException(400, detail="invalid cmd")

    # (옵션) 명령을 테이블에 적재
    with _conn() as c:
        c.execute("""
            INSERT INTO kdemon_commands (cmd, args_json, created_at)
            VALUES (?, ?, ?)
        """, (cmd, (body.args and json.dumps(body.args)) or None, now_ymdhms()))
        c.commit()

    demon = KDemon.get(config.DB_PATH, poll_interval_sec=5, dry_run=config.KDEMON_DRY_RUN)
    if cmd == "start":
        await demon.start()
    elif cmd == "stop":
        await demon.stop()
    elif cmd == "refresh":
        await demon.refresh()

    return {"ok": True, "cmd": cmd}

@router.get("/status")
def status():
    with _conn() as c:
        row = c.execute("SELECT status, updated_at FROM kdemon_state WHERE id=1").fetchone()
        cur = c.execute("SELECT COUNT(*) FROM kdemon_rules WHERE status='active'").fetchone()
    return {
        "status": row[0] if row else "unknown",
        "updated_at": row[1] if row else None,
        "active_rules": cur[0] if cur else 0
    }
