FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Command for SSE transport (running via uvicorn)
# Or for standard stdio depending on the MCP platform
CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8080"]
