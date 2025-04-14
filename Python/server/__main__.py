from mcp.server.fastmcp import FastMCP
from .core import server_lifespan, logger

# Import and register tools
from .tools.actor_tools import register_actor_tools
from .tools.editor_tools import register_editor_tools
from .tools.blueprint_tools import register_blueprint_tools
from .tools.node_tools import register_blueprint_node_tools


# Initialize server
mcp = FastMCP(
    "UnrealMCP",
    description="Unreal Engine integration via Model Context Protocol",
    lifespan=server_lifespan,
)

# Register tools
register_actor_tools(mcp)
register_editor_tools(mcp)
register_blueprint_tools(mcp)
register_blueprint_node_tools(mcp)


@mcp.prompt()
def unreal_best_practices():
    """Best practices for working with Unreal MCP."""
    return """
    # Unreal MCP Server Tools and Best Practices
    
    ## Actor Management
    - ALWAYS use `find_actors_by_name(name)` to check if an actor exists before creating or modifying it
    - `create_actor(name, type, location, rotation, scale)` - Create actors (e.g. `CUBE`, `SPHERE`, `CAMERA`, `LIGHT`)
    - `delete_actor(name)` - Remove actors
    - `set_actor_transform(name, location, rotation, scale)` - Modify actor position, rotation, and scale
    - `get_actor_properties(name)` - Get actor properties
    - `get_actors_in_level()` - Get all actors in the current level
    
    ## Blueprint Management
    - `create_blueprint(name, parent_class)` - Create new Blueprint classes
    - `add_component_to_blueprint(blueprint_name, component_type, component_name, location, rotation, scale)` - Add components to Blueprints
    - `set_component_property(blueprint_name, component_name, property_name, property_value)` - Set component properties
    - `set_physics_properties(blueprint_name, component_name, simulate_physics, gravity_enabled, mass, linear_damping, angular_damping)` - Configure physics
    - `compile_blueprint(blueprint_name)` - Compile Blueprint changes
    - `set_blueprint_property(blueprint_name, property_name, property_value)` - Set Blueprint class properties
    - `set_pawn_properties(blueprint_name, auto_possess_player, use_controller_rotation_yaw, use_controller_rotation_pitch, use_controller_rotation_roll, can_be_damaged)` - Configure Pawn settings
    - `spawn_blueprint_actor(blueprint_name, actor_name, location, rotation, scale)` - Spawn Blueprint actors in the level
    
    ## Blueprint Node Management
    - `add_blueprint_event_node(blueprint_name, event_type, node_position)` - Add event nodes (BeginPlay, Tick, etc.)
    - `add_blueprint_input_action_node(blueprint_name, action_name, node_position)` - Add input action nodes
    - `add_blueprint_function_node(blueprint_name, target, function_name, params, node_position)` - Add function call nodes
    - `connect_blueprint_nodes(blueprint_name, source_node_id, source_pin, target_node_id, target_pin)` - Connect nodes
    - `add_blueprint_variable(blueprint_name, variable_name, variable_type, default_value, is_exposed)` - Add variables
    - `create_input_mapping(action_name, key, input_type)` - Create input mappings
    - `add_blueprint_get_self_component_reference(blueprint_name, component_name, node_position)` - Add component references
    - `add_blueprint_self_reference(blueprint_name, node_position)` - Add self references
    - `find_blueprint_nodes(blueprint_name, node_type, event_type)` - Find nodes in Blueprint graphs
    
    ## Editor Tools
    - `focus_viewport(target, location, distance, orientation)` - Focus viewport on actors or locations
    - `take_screenshot(filename, show_ui, resolution)` - Capture viewport screenshots
    
    ## Best Practices
    ### Actor Creation and Management
    - When creating actors, always provide a unique name to avoid conflicts
    - Valid actor types include: CUBE, SPHERE, PLANE, CYLINDER, CONE, CAMERA, LIGHT, POINT_LIGHT, SPOT_LIGHT
    - Location is specified as [x, y, z] in Unreal units
    - Rotation is specified as [pitch, yaw, roll] in degrees
    - Scale is specified as [x, y, z] multipliers (1.0 is default scale)
    - Always clean up temporary actors when no longer needed
    
    ### Blueprint Development
    - Always compile Blueprints after making changes
    - Use meaningful names for variables and functions
    - Organize nodes in the graph for better readability
    - Test Blueprint functionality in a controlled environment
    - Use proper variable types for different data needs
    - Consider performance implications when adding nodes
    
    ### Node Graph Management
    - Position nodes logically to maintain graph readability
    - Use appropriate node types for different operations
    - Connect nodes with proper pin types
    - Document complex node setups with comments
    - Test node connections before finalizing
    
    ### Input Mapping
    - Use descriptive names for input actions
    - Consider platform-specific input needs
    - Test input mappings thoroughly
    - Document input bindings for team reference
    
    ### Error Handling
    - Always check command responses for success status
    - Handle error cases gracefully
    - Log important operations and errors
    - Validate parameters before sending commands
    - Clean up resources in error cases
    """


# Run the server
if __name__ == "__main__":
    logger.info("Starting MCP server with stdio transport")
    # Use stdio transport as websocket is likely not supported either
    mcp.run(transport="stdio")
