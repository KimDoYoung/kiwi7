# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Kiwi7 is a Korean stock trading web application that uses Kiwoom Securities' RESTful API (with KIS and LS Securities support in development). The application is designed to run in Docker on a local PC, with a FastAPI backend and Alpine.js frontend on port 8001.

## Development Commands

```bash
# Install dependencies
uv sync

# Run development server
uvicorn backend.main:app --host 0.0.0.0 --port 8002 --reload

# Run all tests
pytest

# Run specific test categories
pytest -m unit           # Unit tests only
pytest -m api            # API tests only
pytest -m integration    # Integration tests only
pytest -m "not slow"     # Exclude slow tests

# Run single test file or specific test
pytest tests/unit/test_config.py
pytest tests/unit/test_config.py::test_config_default_values

# Coverage report
pytest --cov=backend --cov-report=html

# Lint with ruff
ruff check .
ruff format .

# Docker
docker-compose up -d
docker logs -f kiwi7-app
```

## Coding Conventions

- **Comments and logs in Korean**: All code comments (`# 한글 주석`) and logger messages (`logger.info("한글 메시지")`) should be in Korean
- **Package manager**: Use `uv` as the primary package manager (not pip)
- **Line length**: 100 characters (ruff config)
- **Quotes**: Single quotes preferred
- **No jQuery**: Frontend uses Alpine.js only
- **Type hints required**: Use typing module annotations

## Architecture

### Backend Structure

```
backend/
├── main.py                  # Entry point, middleware, route registration
├── core/                    # Infrastructure (config, JWT, security, DB, logging)
├── api/v1/endpoints/        # Route handlers
├── domains/                 # Business logic
│   ├── kscheduler/          # Async task scheduler (persistence, cron, concurrency)
│   ├── kdemon/              # Rule-based automated trading daemon
│   ├── kiwoom/              # Kiwoom API (REST + WebSocket)
│   ├── services/            # Business services (one per table)
│   └── models/              # Pydantic models (one per table)
├── page_contexts/           # Jinja2 template context providers
└── utils/
```

### Frontend Structure

```
frontend/
├── public/js/fetchUtil.js   # AJAX utility (GET/POST/PUT/DELETE, KiwiError handling)
└── views/template/          # Jinja2 templates with Alpine.js
```

### Key Integration Points

**Kiwoom API calls** (see `backend/domains/models/kiwoom_request_definition.py` and `kiwoom_response_definition.py`):
```python
kiwoom_api = await get_kiwoom_api()
response = await kiwoom_api.send_request(KiwoomRequest(api_id="ka10099", payload={"mrkt_tp": mrkt_tp}))
```

**Service pattern**:
```python
service = get_service("settings")
result = await service.get(SettingsKey.LAST_STK_INFO_FILL)
```

**Template page routing**: `/page?path=stock/find` → `frontend/views/template/stock/find.html`
- Context providers registered in `backend/page_contexts/context_registry.py`

### Authentication

Cookie-based JWT (NOT Bearer header):
- Cookie name: `kiwi7_token`
- Middleware: `JWTAuthMiddleware`
- Bypassed paths: `/public`, `/favicon.ico`, `/login`, `/logout`

### Database

SQLite with schema in `sqls/kiwi7_ddl.sql`. Auto-created on startup.

When adding a new table:
1. Add DDL to `sqls/kiwi7_ddl.sql`
2. Create Pydantic model in `backend/domains/models/{table}_model.py`
3. Create service in `backend/domains/services/{table}_service.py`

### HTML Template Pattern

```html
{% extends 'common/base.html' %}
{% block content %}
<div x-data="componentName" class="container mt-4">
</div>
{% endblock %}
{% block script %}
{% raw %}
<script>
function createComponent() {
    return {
        data: null,
        init() { console.log('Initializing'); }
    };
}
document.addEventListener('alpine:init', () => {
    Alpine.data('componentName', createComponent);
});
</script>
{% endraw %}
{% endblock %}
```

## Environment Configuration

Profile-based using `.env.{PROFILE}` files (default: `.env.local`). Set `KIWI7_MODE` to change profile.

Key variables:
- `BASE_DIR`, `DB_PATH`, `LOG_DIR`: Paths configuration
- `KIWOOM_APP_KEY`, `KIWOOM_SECRET_KEY`, `KIWOOM_ACCT_NO`: Kiwoom API credentials
- `JWT_SECRET_KEY`: Authentication

## Test Markers

Defined in `pyproject.toml`:
- `@pytest.mark.unit` - Unit tests
- `@pytest.mark.integration` - Integration tests
- `@pytest.mark.api` - API endpoint tests
- `@pytest.mark.slow` - Long-running tests

For async tests: `@pytest.mark.asyncio`

Skip real API calls with `@pytest.mark.skip`
