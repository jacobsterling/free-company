# MCP Game Project

This is an Unreal Engine project that uses the Mission Control Protocol (MCP) to automate various tasks in the editor.

## Project Structure

- `mcp/` - Contains the Mission Control Protocol implementation
  - `scripts/` - Python scripts for the MCP
  - `Makefile` - Unix/Linux/macOS build script
  - `mcp.bat` - Windows batch script
  - `README.md` - Documentation for the MCP
- `mcp-launcher.bat` - Windows launcher script (delegates to mcp/mcp.bat)

## Getting Started

### Prerequisites

- Unreal Engine 5.x
- Python 3.12+ (required for the MCP)

### Setting Up the Virtual Environment

The MCP uses a Python 3.12+ virtual environment to manage dependencies. The virtual environment is created in the `.venv` directory.

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

### Running the MCP Server

**On Unix/Linux/macOS:**
```bash
make start-server
```

**On Windows:**
```cmd
mcp-launcher start-server
```

### Setting Up the Game Mode

```bash
make setup-game
```

## Development

See the [MCP README](mcp/README.md) for information on developing with the MCP.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 