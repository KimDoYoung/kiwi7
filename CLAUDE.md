# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Kiwi7 is a Korean stock trading web application that uses Kiwoom Securities' RESTful API. The application is designed to run in Docker on a local PC, with a FastAPI backend and Alpine.js frontend on port 8001.

## Technology Stack

- **Python**: 3.12 with `uv` package manager
- **Backend**: FastAPI, Uvicorn, Jinja2, SQLite3, JWT, Pydantic, python-dotenv, aiohttp
- **Frontend**: Alpine.js, Bootstrap 5, HTML5
- **Deployment**: Docker

## Development Commands

### Running the Application

```bash
# Run with uvicorn directly (development)
uvicorn backend.main:app --host 0.0.0.0 --port 8001 --reload

# Run with Docker Compose
docker-compose up -d

# Build Docker image
docker build -t kiwi7-img .
```

### Database

The application uses SQLite3 with schema defined in `sqls/kiwi7_ddl.sql`. Database is automatically created on startup at the path specified in configuration (default: `c:\kiwi7\db\kiwi7.db`).

## Architecture

### Backend Structure

The backend follows a clean architecture pattern with clear separation of concerns:

```
backend/
├── main.py                  # Application entry point, middleware setup, route registration
├── core/                    # Core infrastructure components
│   ├── config.py           # Environment-based configuration (.env.{PROFILE})
│   ├── jwtmiddleware.py    # JWT authentication (cookie-based, no Bearer header)
│   ├── security.py         # Token creation and verification
│   ├── kiwi7_db.py         # Database initialization
│   ├── logger.py           # Logging configuration
│   ├── template_engine.py  # Jinja2 template rendering
│   └── exception_handler.py
├── api/v1/endpoints/       # API route handlers
│   ├── home_routes.py      # Main pages (/main, /login, /logout)
│   ├── kiwoom_routes.py    # Kiwoom API integration
│   ├── kdemon_routes.py    # Automated trading rules
│   ├── scheduler_routes.py # Job scheduling
│   ├── stock_routes.py     # Stock information
│   ├── mystock_routes.py   # Personal stock portfolio
│   └── diary_routes.py     # Trading diary
├── domains/                # Business logic and domain models
│   ├── kscheduler/         # Time-based job orchestration
│   ├── kdemon/             # Rule-based automated trading
│   ├── kiwoom/             # Kiwoom API wrapper (REST + WebSocket)
│   ├── services/           # Business services
│   ├── models/             # Data models
│   └── user/               # User management
├── page_contexts/          # Context providers for Jinja2 templates
└── utils/                  # Utility functions
```

### Frontend Structure

```
frontend/
├── public/                 # Static assets (CSS, JS, images)
│   ├── css/               # Bootstrap and custom styles
│   ├── js/                # Alpine.js components and utilities
│   └── images/
└── views/                  # HTML templates
    ├── main.html          # Main dashboard
    ├── login.html         # Login page
    └── template/          # Reusable page fragments
```

### Key Domain Components

#### KScheduler (backend/domains/kscheduler/k_scheduler.py)

A custom async task scheduler with the following features:

- **Persistence**: Jobs stored in SQLite, survive restarts
- **Schedule Types**: interval, cron (simplified), once (at specific time)
- **Concurrency Control**: max_concurrency, overlap_policy (skip/queue/cancel)
- **Safety**: timeout, retry with exponential backoff, jitter
- **Multi-process Support**: Lock table prevents duplicate execution
- **Trading Hours Integration**: Gating callbacks control job execution based on market hours
- All jobs must be async functions

Started automatically on application startup with 4 workers.

#### KDemon (backend/domains/kdemon/k_demon.py)

Rule-based automated trading daemon that:

- Periodically polls stock prices
- Evaluates conditions from database rules (e.g., "sell 10 shares if price > 100")
- Executes trades automatically
- Supports cooldown periods and validity time windows
- Can run in dry-run mode for testing

#### Kiwoom Integration (backend/domains/kiwoom/)

- **kiwoom_rest_api.py**: REST API wrapper for Kiwoom Securities
- **kiwoom_ws_client.py**: WebSocket client for real-time data
- **managers/**: Token management and API call orchestration
- **models/**: Request/response models for Kiwoom API

Kiwoom API credentials are stored in environment variables: `KIWOOM_APP_KEY`, `KIWOOM_SECRET_KEY`, `KIWOOM_ACCT_NO`.

### Configuration and Environment

Configuration is environment-based using `.env.{PROFILE}` files where PROFILE defaults to 'local':

- Set `KIWI7_MODE` environment variable to change profile (e.g., 'docker', 'prod')
- Important config values:
  - `BASE_DIR`: Base directory for data/logs/db (default: c:\kiwi7)
  - `DB_PATH`: SQLite database path
  - `LOG_LEVEL`, `LOG_DIR`: Logging configuration
  - `JWT_SECRET_KEY`, `ALGORITHM`: JWT authentication
  - `KIWOOM_*`: Kiwoom API credentials

### Authentication Flow

The application uses a **cookie-based JWT authentication** system (NOT Bearer header):

1. User logs in via POST `/login`
2. JWT token created and set as HTTP-only cookie (name: `kiwi7_token`)
3. `JWTAuthMiddleware` validates token from cookie on each request
4. Invalid/missing token redirects to `/login`
5. Static paths (`/public`, `/favicon.ico`) and `/login`, `/logout` bypass authentication

### Template Rendering

Pages use Jinja2 templates with dynamic context providers:

- Templates located in `frontend/views/`
- Context providers registered in `backend/page_contexts/context_registry.py`
- Common pattern: `/main` renders full page, `/api/v1/{resource}` returns JSON
- Template fragments can be requested via `/template?path={page}` for AJAX updates

### Database Schema

Key tables (see `sqls/kiwi7_ddl.sql` for full schema):

- **mystock**: Personal stock portfolio (holdings and watchlist)
- **stock_history**: Buy/sell transaction history
- **kdemon_rules**: Automated trading rules
- **scheduler_jobs**: Scheduled job definitions
- **scheduler_runs**: Job execution history
- **settings**: Key-value configuration storage
- **users**: User accounts

## Development Practices

### Working with Services

Business logic resides in `backend/domains/services/`:

- Services follow dependency injection pattern (see `dependency.py`)
- Each service handles a specific domain (stocks, scheduler, diary, etc.)
- Services interact with database directly using sqlite3

### Adding New Routes

1. Create route handler in `backend/api/v1/endpoints/{name}_routes.py`
2. Register router in `backend/main.py` in `add_routes()` function
3. Follow existing patterns for authentication and error handling

### Modifying the Scheduler

KScheduler jobs are managed via:

- Database: Insert/update jobs in `scheduler_jobs` table
- API: Use `/api/v1/scheduler` endpoints
- All job functions must be async and accept `**kwargs`

### Frontend Development

- Alpine.js components use `x-data`, `x-show`, `x-if` directives
- Bootstrap 5 provides styling foundation
- AJAX calls use fetch API with JWT cookie automatically included
- Public static files served from `/public` path

## Utilities

### code_samples/extract_kw_req_def.py

Utility to extract request definitions from Kiwoom API Excel documentation:

```bash
python code_samples/extract_kw_req_def.py c:\tmp\kwapi.xlsx > output.txt
```

## Important Notes

- Default port is **8001** (not 8000, despite some legacy references)
- Application designed for single-user local deployment
- Korean market trading hours are checked via `OpentimeChecker` class
- All async operations should respect KRX (Korean Exchange) trading hours
- WebSocket connections for real-time data from Kiwoom are managed separately
