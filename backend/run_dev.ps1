# Vakeel Saab - Development Server Launcher
# Runs uvicorn with autoreload restricted to the app/ directory only,
# excluding .venv, __pycache__, and test artifacts from the file watcher.

.venv\Scripts\uvicorn app.main:app `
    --reload `
    --reload-dir app `
    --host 0.0.0.0 `
    --port 8000 `
    --log-level info
