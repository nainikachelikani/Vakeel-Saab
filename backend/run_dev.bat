@echo off
REM Vakeel Saab - Development Server Launcher
REM Runs uvicorn with autoreload restricted to the app\ directory only.

.venv\Scripts\uvicorn app.main:app ^
    --reload ^
    --reload-dir app ^
    --host 0.0.0.0 ^
    --port 8000 ^
    --log-level info
