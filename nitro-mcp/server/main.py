from fastapi import FastAPI
from mcp.server.sse import SseServerTransport
from mcp.server.fastapi import create_route
from mcp import Server
import uvicorn
import os

app = FastAPI(title="NitroMCP Adapter Server")

# Initialize MCP Server
mcp_server = Server("nitro-mcp")

# Import tools so they register with the decorator
import tools.search
import tools.documents
import tools.drafts

sse = SseServerTransport("/messages")

# Handle SSE connections
app.add_route("/sse", create_route(mcp_server, sse))
app.add_route("/messages", create_route(mcp_server, sse))

@app.on_event("startup")
async def startup():
    print("NitroMCP Server starting up, exposing Stdio and SSE endpoints.")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    uvicorn.run("server.main:app", host="0.0.0.0", port=port, reload=True)
