# Vakeel Saab Backend

Welcome to the backend server foundation for **Vakeel Saab**, an AI-powered multi-agent legal intelligence platform.

## Technology Stack

- **Python**: 3.12+
- **Framework**: FastAPI
- **Database**: PostgreSQL (SQLAlchemy 2.0 ORM & Alembic migrations)
- **Validation**: Pydantic v2
- **Environment Management**: python-dotenv

---

## Directory Structure

```text
backend/
├── app/
│   ├── api/             # API routes and endpoints
│   │   ├── auth/        # Authentication routes
│   │   ├── chat/        # Multi-agent chat session routes
│   │   ├── documents/   # Document search & analysis routes
│   │   ├── reports/     # Legal reports routes
│   │   ├── mcp/         # Model Context Protocol endpoints
│   │   └── admin/       # Administrative management routes
│   │
│   ├── agents/          # Multi-agent autonomous system
│   │   ├── router/      # Intent Router agent
│   │   ├── domain/      # Domain specific expert agents
│   │   ├── retrieval/   # Document retriever agent (RAG)
│   │   ├── legal_analysis/ # Deep legal analysis agent
│   │   ├── citation/    # Citation verifying agent
│   │   ├── planner/     # Action planning agent
│   │   └── reviewer/    # Quality assurance agent
│   │
│   ├── config/          # Central settings and logging initialization
│   ├── database/        # Engines, sessions, and schemas base
│   ├── models/          # Declarative relational models
│   ├── schemas/         # Serialization & request validation schemas
│   ├── rag/             # Vector embeddings & database retrievers
│   ├── services/        # Business logic layer
│   ├── utils/           # Helper scripts & custom wrappers
│   └── main.py          # Application entrypoint
│
├── tests/               # Test suites
├── requirements.txt     # Locked project dependencies
└── .env.example         # System configurations variables template
```

---

## Getting Started

### Prerequisites

Ensure you have Python 3.12+ installed local.

### Installation

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - **Windows (PowerShell)**:
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - **macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Create a `.env` file by copying the example template:
```bash
cp .env.example .env
```
And adjust database connection strings and parameters inside `.env`.

### Running Server

**Recommended** — Use the provided launcher script which restricts autoreload to `app/` only, preventing reload loops caused by `.venv` and `__pycache__`:

```powershell
# PowerShell
.\run_dev.ps1
```

```cmd
:: Command Prompt
run_dev.bat
```

Alternatively, run uvicorn directly with the same flags:

```powershell
.venv\Scripts\uvicorn app.main:app --reload --reload-dir app --host 0.0.0.0 --port 8000
```

> **Why `--reload-dir app`?**  
> Without it, uvicorn watches the entire project directory including `.venv`, causing continuous reload loops whenever pip installs update a package file.

The service starts on `http://127.0.0.1:8000`. Available URLs:
- **Health check**: `http://127.0.0.1:8000/health`
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **Redoc**: `http://127.0.0.1:8000/redoc`

---

## API Testing & Ping Endpoints

Verify services health by requesting ping status APIs:
- GET `/api/v1/auth/ping` -> `{"message": "Auth API working"}`
- GET `/api/v1/chat/ping` -> `{"message": "Chat API working"}`
- GET `/api/v1/documents/ping` -> `{"message": "Documents API working"}`
- GET `/api/v1/reports/ping` -> `{"message": "Reports API working"}`
- GET `/api/v1/mcp/ping` -> `{"message": "MCP API working"}`
- GET `/api/v1/admin/ping` -> `{"message": "Admin API working"}`
