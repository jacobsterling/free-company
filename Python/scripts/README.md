# Free Company Implementation Scripts

This directory contains Python scripts for automating the implementation of the Free Company game as outlined in the phase1_implementation.md document.

## Scripts Overview

- **phase1_implementation.py**: Main script that runs the implementation steps in sequence
- **project_setup.py**: Implements Step 1 - Project Setup and Structure
- **first_person_controller.py**: Implements Step 2 - First-Person Character Controller

## How to Run

1. Make sure Unreal Engine is running with your MCPGameProject open
2. Ensure the MCP (Multiplayer Coding Protocol) server is running in Unreal Engine
3. Run the main implementation script:

```bash
cd "C:/Users/j10st/OneDrive/Documents/Unreal Projects/MCPGameProject/Python/scripts"
python phase1_implementation.py
```

Alternatively, you can run individual steps:

```bash
python project_setup.py     # For Step 1 only
python first_person_controller.py  # For Step 2 only
```

## Script Details

### Step 1: Project Setup and Structure (project_setup.py)
- Creates necessary folders in Content directory
- Sets up basic project settings
- Configures input mappings for WASD, jumping, and interaction

### Step 2: First-Person Character Controller (first_person_controller.py)
- Creates a basic first-person character blueprint
- Implements WASD movement
- Adds jumping functionality
- Creates a basic interaction system
- Implements sprinting
- Adds basic collision detection
- Creates a simple camera system with head bobbing

## Requirements
- Unreal Engine with MCP plugin
- MCP server running on port 55557 (default)
- Python 3.6+

## Troubleshooting
- If scripts fail to connect, ensure the MCP server is running in Unreal Engine
- Check console logs in Unreal Engine for error messages
- Make sure the project is properly set up with the MCP plugin