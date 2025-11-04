# --- kiwi7 Dockerfile ---
FROM python:3.12-slim

# 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TZ=Asia/Seoul

# 필수 패키지 설치
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential gcc libpq-dev curl && \
    rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 생성
WORKDIR /app

# 의존성 복사 및 설치
COPY pyproject.toml ./
RUN pip install --upgrade pip && \
    pip install uv && \
    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi && \
    if [ -f pyproject.toml ]; then pip install .; fi

# 소스 복사
COPY . .

# 포트 노출
EXPOSE 8001

# uvicorn 실행 (FastAPI)
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
