@echo off
echo Starting Unreal MCP Server...

:: Check if virtual environment exists
if not exist mcp_venv (
    echo Virtual environment not found. Creating one...
    python -m venv mcp_venv
    call mcp_venv\Scripts\activate.bat
    pip install -e .
) else (
    call mcp_venv\Scripts\activate.bat
)

:: Clear any previous log file
if exist unreal_mcp.log del unreal_mcp.log

:: Run the server in a way that keeps the console window open
echo Starting MCP server on http://127.0.0.1:8000...
echo Server logs will be written to unreal_mcp.log
echo Press Ctrl+C to stop the server

:: Run the server
python unreal_mcp_server.py

:: Deactivate virtual environment when done
call deactivate
echo Server stopped. 