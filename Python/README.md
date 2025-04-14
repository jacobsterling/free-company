# MCP Game Project Tools and Scripts

This project contains tools and scripts for interacting with the Unreal Engine MCP (Model Context Protocol) plugin. The project is organized into two main directories: `tools/` for MCP command implementations and `scripts/` for example usage and templates.

## Project Structure

```
.
├── tools/                  # MCP command implementations
│   ├── actor_tools.py     # Actor-related commands
│   ├── blueprint_tools.py # Blueprint-related commands
│   ├── editor_tools.py    # Editor-related commands
│   ├── node_tools.py      # Blueprint node-related commands
│   └── __init__.py        # Tool registration
│
└── scripts/               # Example scripts and templates
    ├── actors/           # Actor-related example scripts
    ├── blueprints/       # Blueprint-related example scripts
    └── node/             # Node-related example scripts
```

## Tools Directory

The `tools/` directory contains the core implementations of MCP commands. Each tool file focuses on a specific aspect of Unreal Engine interaction:

### Available Tools

1. **Actor Tools** (`actor_tools.py`)
   - Create, modify, and manage actors in the scene
   - Handle actor properties and transformations
   - Manage actor lifecycle

2. **Blueprint Tools** (`blueprint_tools.py`)
   - Create and modify Blueprint classes
   - Manage Blueprint components
   - Handle Blueprint compilation

3. **Editor Tools** (`editor_tools.py`)
   - Control the Unreal Editor viewport
   - Take screenshots
   - Manage editor state

4. **Node Tools** (`node_tools.py`)
   - Create and connect Blueprint nodes
   - Manage node graphs
   - Handle node properties and connections

### Creating New Tools

To create a new tool:

1. Create a new Python file in the `tools/` directory
2. Define your tool functions using the MCP decorator pattern:

```python
from mcp.server.fastmcp import FastMCP

def register_my_tools(mcp: FastMCP):
    @mcp.tool()
    def my_new_tool(param1: str, param2: int) -> dict:
        """
        Description of what the tool does.
        
        Args:
            param1: Description of first parameter
            param2: Description of second parameter
            
        Returns:
            dict: Description of return value
        """
        # Tool implementation
        return {"status": "success", "result": "operation completed"}
```

3. Register your tools in `tools/__init__.py`:

```python
from .my_tools import register_my_tools

def register_all_tools(mcp):
    register_my_tools(mcp)
    # ... other tool registrations
```

## Scripts Directory

The `scripts/` directory contains example scripts and templates for using the MCP tools. These scripts demonstrate how to use the tools in different scenarios.

### Script Categories

1. **Actors** (`scripts/actors/`)
   - Examples of actor creation and manipulation
   - Actor property management
   - Scene setup scripts

2. **Blueprints** (`scripts/blueprints/`)
   - Blueprint class creation examples
   - Component management
   - Blueprint compilation workflows

3. **Nodes** (`scripts/node/`)
   - Node graph creation examples
   - Node connection patterns
   - Custom node setup

### Creating New Scripts

To create a new script:

1. Choose the appropriate category directory
2. Create a new Python file with a descriptive name
3. Import the necessary tools and implement your script:

```python
from tools.actor_tools import create_actor, set_actor_transform
from tools.blueprint_tools import create_blueprint, add_component_to_blueprint

def main():
    # Create a new actor
    actor = create_actor("MyActor", "CUBE", [0, 0, 0], [0, 0, 0], [1, 1, 1])
    
    # Create a blueprint
    blueprint = create_blueprint("MyBlueprint", "Actor")
    
    # Add components
    add_component_to_blueprint(blueprint, "StaticMeshComponent", "Mesh", [0, 0, 0], [0, 0, 0], [1, 1, 1])

if __name__ == "__main__":
    main()
```

## Running Scripts

To run a script:

1. Ensure the MCP server is running:
```bash
make start-server
```

2. Run your script:
```bash
python scripts/your_script.py
```

## Best Practices

1. **Tool Development**
   - Keep tools focused and single-purpose
   - Provide clear documentation for parameters and return values
   - Handle errors gracefully and return meaningful error messages
   - Use type hints for better code clarity

2. **Script Development**
   - Use meaningful variable names
   - Comment complex operations
   - Break down large operations into smaller functions
   - Include error handling
   - Add logging for debugging

3. **Testing**
   - Test tools with various parameter combinations
   - Verify script behavior in different scenarios
   - Clean up any created objects after testing

## Common Patterns

### Actor Creation Pattern
```python
# Create actor with transform
actor = create_actor(
    name="MyActor",
    actor_type="CUBE",
    location=[0, 0, 0],
    rotation=[0, 0, 0],
    scale=[1, 1, 1]
)

# Modify transform
set_actor_transform(
    name="MyActor",
    location=[100, 0, 0],
    rotation=[0, 45, 0],
    scale=[2, 2, 2]
)
```

### Blueprint Creation Pattern
```python
# Create blueprint
blueprint = create_blueprint(
    name="MyBlueprint",
    parent_class="Actor"
)

# Add component
add_component_to_blueprint(
    blueprint_name="MyBlueprint",
    component_type="StaticMeshComponent",
    component_name="Mesh",
    location=[0, 0, 0],
    rotation=[0, 0, 0],
    scale=[1, 1, 1]
)

# Compile blueprint
compile_blueprint("MyBlueprint")
```

### Node Graph Pattern
```python
# Add event node
event_node = add_blueprint_event_node(
    blueprint_name="MyBlueprint",
    event_type="BeginPlay",
    node_position=[0, 0]
)

# Add function node
function_node = add_blueprint_function_node(
    blueprint_name="MyBlueprint",
    target="Self",
    function_name="MyFunction",
    params={},
    node_position=[200, 0]
)

# Connect nodes
connect_blueprint_nodes(
    blueprint_name="MyBlueprint",
    source_node_id=event_node["node_id"],
    source_pin="exec",
    target_node_id=function_node["node_id"],
    target_pin="exec"
)
``` 