@echo off
REM MCP Game Project Batch File
REM This batch file provides commands for running the MCP server and other common operations

REM Python virtual environment settings
set VENV_DIR=..\.venv
set PYTHON=%VENV_DIR%\Scripts\python.exe
set PIP=%VENV_DIR%\Scripts\pip.exe
set PYTHON_VERSION=3.12

if "%1"=="" goto help
if "%1"=="help" goto help
if "%1"=="setup-venv" goto setup-venv
if "%1"=="start-server" goto start-server
if "%1"=="stop-server" goto stop-server
if "%1"=="restart-server" goto restart-server
if "%1"=="test-server" goto test-server
if "%1"=="test-client" goto test-client
if "%1"=="setup-game" goto setup-game
if "%1"=="test" goto test
if "%1"=="clean" goto clean
goto help

:help
echo MCP Game Project Batch File
echo.
echo Available commands:
echo   mcp setup-venv     - Set up the Python virtual environment
echo   mcp start-server   - Start the MCP server
echo   mcp stop-server    - Stop the MCP server
echo   mcp restart-server - Restart the MCP server
echo   mcp test-server    - Run the test server
echo   mcp test-client    - Run the test client
echo   mcp setup-game     - Run the game mode setup script
echo   mcp test           - Run all tests with pytest
echo   mcp clean          - Clean up temporary files
echo   mcp help           - Show this help message
goto :eof

:setup-venv
echo Setting up Python virtual environment...
if not exist %VENV_DIR% (
    echo Creating Python %PYTHON_VERSION% virtual environment...
    python -m venv %VENV_DIR% --clear
    call %PIP% install -e ..
) else (
    echo Virtual environment already exists.
)
echo Virtual environment setup complete.
goto :eof

:start-server
call :setup-venv
echo Starting MCP server...
call %PYTHON% -m mcp.server
goto :eof

:stop-server
echo Stopping MCP server...
if exist unreal_mcp.pid (
    for /f "tokens=*" %%a in (unreal_mcp.pid) do (
        taskkill /F /PID %%a 2>nul
    )
    del unreal_mcp.pid
    echo MCP server stopped.
) else (
    echo No MCP server PID file found. Server may not be running.
)
goto :eof

:restart-server
call mcp stop-server
call mcp start-server
goto :eof

:test-server
call :setup-venv
echo Running test server...
call %PYTHON% scripts/tests/test_server.py
goto :eof

:test-client
call :setup-venv
echo Running test client...
call %PYTHON% scripts/tests/test_client.py
goto :eof

:test
call :setup-venv
echo Running all tests with pytest...
call %PYTHON% -m pytest
goto :eof

:setup-game
call :setup-venv
echo Setting up game mode...
call %PYTHON% scripts/game/setup_game_mode.py
goto :eof

:clean
echo Cleaning up temporary files...
if exist unreal_mcp.log del unreal_mcp.log
if exist unreal_mcp.pid del unreal_mcp.pid
echo Cleanup complete.
goto :eof 