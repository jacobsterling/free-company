@echo off
REM MCP Game Project Launcher
REM This batch file is a simple launcher that delegates to the main batch file in the mcp folder

if "%1"=="" goto help
if "%1"=="help" goto help
goto run-command

:help
echo MCP Game Project Launcher
echo.
echo This launcher delegates to the main batch file in the mcp folder.
echo Available commands:
echo   mcp setup-venv     - Set up the Python virtual environment
echo   mcp start-server   - Start the MCP server
echo   mcp stop-server    - Stop the MCP server
echo   mcp restart-server - Restart the MCP server
echo   mcp test-server    - Run the test server
echo   mcp test-client    - Run the test client
echo   mcp setup-game     - Run the game mode setup script
echo   mcp clean          - Clean up temporary files
echo   mcp help           - Show this help message
goto :eof

:run-command
cd mcp
call mcp.bat %*
cd ..
goto :eof 