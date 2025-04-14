# MCP Game Project Makefile

# Python virtual environment settings
PYTHON_DIR = Python
VENV_DIR = $(PYTHON_DIR)/mcp_venv
PYTHON = $(VENV_DIR)\Scripts\python.exe
PIP = $(VENV_DIR)\Scripts\pip.exe

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
	@echo "  make install-deps   - Install dependencies in the virtual environment"
	@echo "  make start-server   - Start the MCP server"
	@echo "  make clean          - Clean up temporary files and logs"
	@echo "  make help           - Show this help message"

# Virtual environment setup
.PHONY: setup-venv
setup-venv:
	@echo "Setting up Python virtual environment..."
	cd $(PYTHON_DIR) && python -m venv mcp_venv
	@echo "Virtual environment created successfully."

# Install dependencies
.PHONY: install-deps
install-deps:
	@echo "Installing dependencies..."
	@"$(PYTHON)" -m pip install --upgrade pip
	cd $(PYTHON_DIR) && "mcp_venv\Scripts\python.exe" -m pip install -e .
	@echo "Dependencies installed successfully."

# Start server
.PHONY: start-server
start-server:
	@echo "Starting MCP server using batch file..."
	cd $(PYTHON_DIR) && cmd /c start_server.bat

# Cleanup
.PHONY: clean
clean:
	@echo "Cleaning up temporary files..."
	-@if exist "$(PYTHON_DIR)\unreal_mcp.log" del "$(PYTHON_DIR)\unreal_mcp.log"
	@echo "Cleanup complete."

# Full cleanup (including virtual environment)
.PHONY: clean-all
clean-all: clean
	@echo "Removing virtual environment..."
	-rd /s /q "$(VENV_DIR)" 2>nul
	@echo "Full cleanup complete."