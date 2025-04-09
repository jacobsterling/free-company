# MCP Game Project Root Makefile
# This Makefile delegates to the one in the mcp folder

# Default target
.PHONY: all
all: help

# Help command
.PHONY: help
help:
	@echo "MCP Game Project Root Makefile"
	@echo ""
	@echo "This Makefile delegates to the one in the mcp folder."
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
	@cd mcp && make setup-venv

# Server commands
.PHONY: start-server
start-server:
	@cd mcp && make start-server

.PHONY: stop-server
stop-server:
	@cd mcp && make stop-server

.PHONY: restart-server
restart-server:
	@cd mcp && make restart-server

# Test commands
.PHONY: test-server
test-server:
	@cd mcp && make test-server

.PHONY: test-client
test-client:
	@cd mcp && make test-client

# Testing
.PHONY: test
test:
	@cd mcp && make test

# Game setup
.PHONY: setup-game
setup-game:
	@cd mcp && make setup-game

# Cleanup
.PHONY: clean
clean:
	@cd mcp && make clean 