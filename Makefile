# MCP Game Project Makefile

# Python virtual environment settings
VENV_DIR = mcp/.venv
PYTHON = $(VENV_DIR)/Scripts/python.exe
PIP = $(VENV_DIR)/Scripts/pip.exe
PYTHON_VERSION = 3.12

# Default target
.PHONY: all
all: help

# Help command
.PHONY: help
help:
	@echo "MCP Game Project Makefile"
	@echo ""
	@echo "Available commands:"
	@echo "  make setup-venv     - Set up the Python virtual environment"
	@echo "  make start-server   - Start the MCP server"
	@echo "  make stop-server    - Stop the MCP server"
	@echo "  make restart-server - Restart the MCP server"
	@echo "  make test-server    - Run the test server"
	@echo "  make test-client    - Run the test client"
	@echo "  make setup-game     - Run the game mode setup script"
	@echo "  make test           - Run all tests with pytest"
	@echo "  make clean          - Clean up temporary files"
	@echo "  make help           - Show this help message"

# Virtual environment setup
.PHONY: setup-venv
setup-venv:
	@echo "Setting up Python virtual environment..."
	@if not exist $(VENV_DIR) (
		@echo "Creating Python $(PYTHON_VERSION) virtual environment..."
		@python -m venv $(VENV_DIR) --clear
		@cd mcp && $(PIP) install -e .
	) else (
		@echo "Virtual environment already exists."
	)
	@echo "Virtual environment setup complete."

# Server commands
.PHONY: start-server
start-server:
	@echo "Starting MCP server..."
	@$(PYTHON) -m mcp.server

.PHONY: stop-server
stop-server:
	@echo "Stopping MCP server..."
	@if exist mcp/unreal_mcp.pid (
		@for /f "tokens=*" %%a in (mcp/unreal_mcp.pid) do (
			@taskkill /F /PID %%a 2>nul
		)
		@del mcp/unreal_mcp.pid
		@echo "MCP server stopped."
	) else (
		@echo "No MCP server PID file found. Server may not be running."
	)

.PHONY: restart-server
restart-server: stop-server start-server

# Test commands
.PHONY: test-server
test-server:
	@echo "Running test server..."
	@$(PYTHON) mcp/scripts/tests/test_server.py

.PHONY: test-client
test-client:
	@echo "Running test client..."
	@$(PYTHON) mcp/scripts/tests/test_client.py

# Testing
.PHONY: test
test:
	@echo "Running all tests with pytest..."
	@$(PYTHON) -m pytest

# Game setup
.PHONY: setup-game
setup-game:
	@echo "Setting up game mode..."
	@$(PYTHON) mcp/scripts/game/setup_game_mode.py

# Cleanup
.PHONY: clean
clean:
	@echo "Cleaning up temporary files..."
	@if exist mcp/unreal_mcp.log del mcp/unreal_mcp.log
	@if exist mcp/unreal_mcp.pid del mcp/unreal_mcp.pid
	@echo "Cleanup complete." 