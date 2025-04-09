# Free Company

An Unreal Engine project for managing and developing a free company system.

## Description
This project is built using Unreal Engine and aims to provide a comprehensive system for managing free companies, including features for company management, member interactions, and gameplay mechanics.

## Project Structure
```
MCPGameProject/
├── Content/
│   ├── Characters/     # Character models and animations
│   ├── Environments/   # Environment assets and levels
│   ├── Blueprints/     # Blueprint classes
│   ├── Materials/      # Material assets
│   ├── Meshes/         # Static and skeletal meshes
│   ├── UI/             # User interface elements
│   └── VFX/            # Visual effects
├── Source/
│   └── MCPGameProject/ # C++ source code
├── scripts/            # MCP automation scripts
│   ├── actors/         # Actor-related scripts
│   ├── blueprints/     # Blueprint-related scripts
│   ├── node/           # Blueprint node scripts
│   ├── create_character.py      # Character creation script
│   ├── setup_character_input.py # Character input setup script
│   ├── test_mcp_client.py      # MCP client test script
│   └── unreal_mcp_server.py    # MCP server implementation
└── Docs/               # Project documentation
```

## Getting Started
1. Clone the repository
2. Open the project in Unreal Engine
3. Start the MCP server:
   ```
   python scripts/unreal_mcp_server.py
   ```
4. Run the character creation script:
   ```
   python scripts/create_character.py
   ```
5. Set up character input:
   ```
   python scripts/setup_character_input.py
   ```
6. Build and run the project

## Requirements
- Unreal Engine 5.x
- Visual Studio 2019 or later (for development)
- Python 3.8 or later (for MCP scripts)
- Required Python packages (install with `pip install -r requirements.txt`):
  - mcp[cli]>=1.4.1
  - fastmcp>=0.2.0
  - uvicorn
  - fastapi
  - pydantic>=2.6.1
  - requests

## MCP Scripts
The project includes several Python scripts for automating Unreal Engine tasks:

- `unreal_mcp_server.py`: MCP server implementation for communicating with Unreal Engine
- `create_character.py`: Creates character blueprints with components
- `setup_character_input.py`: Sets up input handling for characters
- `test_mcp_client.py`: Test client for MCP server

## License
This project is licensed under the MIT License - see the LICENSE file for details. 