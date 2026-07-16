# Vakeel Saab - AI Powered Multi-Agent Legal Intelligence Platform

Welcome to the Vakeel Saab platform. This repository contains a production-ready template configured for parallel development by a four-person engineering team.

## 🚀 How to Run and Test the Application

You can run the application either using Docker (recommended for a full-stack experience) or by running the services individually.

### Option 1: Running with Docker (Recommended)
This is the easiest way to get the entire stack (Frontend, Backend, and Database) running together.

1. Ensure you have Docker and Docker Compose installed on your system.
2. Open a terminal in the root directory (`Vakeel-Saab/`).
3. Run the following command:
   ```bash
   docker-compose up --build
   ```
4. Access the applications:
   - **Frontend (Next.js):** [http://localhost:3000](http://localhost:3000)
   - **Backend API Docs (FastAPI Swagger):** [http://localhost:8000/docs](http://localhost:8000/docs)
   - **Backend API Redoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Option 2: Running Services Individually (For Development)

If you want to run the services separately for active development (which gives you faster hot-reloading and direct console output):

**1. Frontend (Next.js)**
1. Open a terminal and navigate to the frontend directory: `cd frontend`
2. Install dependencies (if not already done): `npm install`
3. Run the development server: `npm run dev`
4. Access the UI at: [http://localhost:3000](http://localhost:3000)

**2. Backend (FastAPI)**
1. Open a new terminal and navigate to the backend directory: `cd backend`
2. Create a virtual environment (optional but recommended): `python -m venv venv` and activate it (e.g., `venv\Scripts\activate` on Windows).
3. Install dependencies: `pip install -r requirements.txt`
4. Run the development server: `uvicorn app.main:app --reload`
5. Access the API docs at: [http://localhost:8000/docs](http://localhost:8000/docs)

*(Note: If running the backend locally without Docker, you will need to ensure a PostgreSQL database is running locally or update the `.env` file to use a SQLite fallback for initial testing if configured.)*

---

## 🌟 Implemented Features Summary

The current scaffold sets up the foundational architecture, UI components, state management, and mock data to allow immediate parallel development. The following features are currently implemented in the frontend using **mock data**:

### 1. Landing & Authentication
- **Landing Page (`/`):** A premium hero section outlining the platform's purpose, with entry points for both Citizen and Professional workflows.
- **Authentication (`/login`, `/signup`):** UI forms for user login and registration, connected to a Zustand state store (`useAuthStore`) and a simulated API service.

### 2. Workflow Selection
- **Role Router (`/select-workflow`):** A clean interface allowing users to branch into either the Citizen Help workflow or the Lawyer Intelligence workflow.

### 3. Citizen Workflow (Get Legal Help)
- **Citizen Dashboard (`/dashboard/citizen`):** An overview page with quick access to legal categories (Civil, Criminal, etc.), the complaint generator, and the AI assistant.
- **Interactive AI Chat (`/dashboard/citizen/chat`):** A chat interface designed to simulate a conversation with the Legal Assistant. It uses a custom hook (`useChat`) and Zustand store to manage conversations, including a "Simulate Dialogue" feature for testing.
- **System Intelligence Monitor:** A side panel in the chat view that visualizes the "thinking" process of the backend AI agents (Router, Domain, Reviewer).
- **Complaint Generator (`/dashboard/citizen/complaint`):** A specialized UI for drafting legal documents (like Police FIRs or Consumer Complaints) with a live preview pane.
- **Nearby Legal Aid (`/dashboard/citizen/nearby-help`):** A directory component to list government resources and free legal clinics.

### 4. Professional Workflow (Analyze Documents)
- **Professional Dashboard (`/dashboard/professional`):** A high-level view for lawyers, showing portfolio risk metrics, recent alerts, and quick access to tools.
- **Workspace Upload (`/dashboard/professional/upload`):** A drag-and-drop file upload interface for ingesting contracts and legal documents.
- **Document Viewer & Risk Analysis (`/dashboard/professional/viewer`, `/dashboard/professional/risk`):** Interfaces to view uploaded PDFs alongside AI-extracted clauses, risk scores (e.g., High Risk indemnity clauses), and compliance checklists.
- **Semantic Search (`/dashboard/professional/search`):** A search interface to query across uploaded archives and case law precedents.
- **Citation Explorer (`/dashboard/professional/citations`):** A tool to verify legal references and view specific statutes (e.g., Indian Contract Act).
- **Reports (`/dashboard/professional/reports`):** A list view of generated legal audits and risk logs with download options.

### 5. Shared Infrastructure
- **Agent Monitor (`/dashboard/agent-monitor`):** A dashboard for supervising the backend Model Context Protocol (MCP) orchestrator and agent logs.
- **Settings & Profile (`/settings`, `/profile`):** Basic user management and app configuration pages.
- **Notifications (`/notifications`):** A central hub for system alerts, document processing statuses, and hearing updates.

---

## 🏗️ Parallel Team Ownership Guidelines

The codebase is structured so your team can work simultaneously without merge conflicts:

- **Frontend Engineer:** Focus on `frontend/src/components` and `frontend/src/app`. The mock data is in `frontend/src/mock/` so you can build out UI functionality without waiting for the backend.
- **Backend API/DB Engineer:** Focus on `backend/app/api`, `backend/app/models`, and `backend/app/services`. Your goal is to replace the mock data endpoints with real database queries using SQLAlchemy.
- **AI/ML Engineer:** Focus on `backend/app/mcp`, `backend/app/agents`, and `backend/app/rag`. The interfaces are defined; you need to plug in the actual LLM calls (e.g., OpenAI/Anthropic), vector database interactions, and MCP tool logic.
- **Integration/DevOps Engineer:** Focus on `docker-compose.yml`, `.env` configurations, `shared/` type definitions, and ensuring the frontend Axios calls (`frontend/src/services/`) properly hit the backend FastAPI routes.
