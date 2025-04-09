# MCP (Mission Control Protocol)

This folder contains the Mission Control Protocol (MCP) implementation for the MCP Game Project. The MCP provides a communication interface between Python scripts and the Unreal Engine editor.

## Structure

- `scripts/` - Contains all the Python scripts for the MCP
  - `core/` - Core server implementation and utilities
  - `game/` - Game-specific commands and setup
  - `blueprints/` - Blueprint-related commands
  - `levels/` - Level-related commands
  - `actors/` - Actor-related commands
  - `input/` - Input-related commands
  - `tests/` - Test scripts
- `Makefile` - Unix/Linux/macOS build script
- `mcp.bat` - Windows batch script

## Virtual Environment

The MCP uses a Python 3.12+ virtual environment to manage dependencies. The virtual environment is created at the root of the project in the `.venv` directory.

### Setting Up the Virtual Environment

**On Unix/Linux/macOS:**
```bash
make setup-venv
```

**On Windows:**
```cmd
mcp-launcher setup-venv
```

This will:
1. Create a Python 3.12+ virtual environment if it doesn't exist
2. Install the project dependencies from pyproject.toml

## Usage

### Starting the Server

**On Unix/Linux/macOS:**
```bash
make start-server
```

**On Windows:**
```cmd
mcp-launcher start-server
```

### Stopping the Server

**On Unix/Linux/macOS:**
```bash
make stop-server
```

**On Windows:**
```cmd
mcp-launcher stop-server
```

### Other Commands

- `setup-venv` - Set up the Python virtual environment
- `restart-server` - Restart the MCP server
- `test-server` - Run the test server
- `test-client` - Run the test client
- `setup-game` - Run the game mode setup script
- `clean` - Clean up temporary files
- `help` - Show available commands

## Development

### Adding New Commands

1. Add the command type to `scripts/core/mcp_utils.py`
2. Implement the command handler in the appropriate module
3. Register the command in `scripts/core/__main__.py`

### Testing

Run the test server and client to verify your changes:

```bash
make test-server
make test-client
```

## Troubleshooting

If you encounter issues with the MCP server:

1. Check the `unreal_mcp.log` file for error messages
2. Make sure no other process is using port 55557
3. Try restarting the server with `make restart-server`
4. If you have dependency issues, try running `make setup-venv` to reinstall dependencies
5. Ensure you have Python 3.12+ installed on your system 