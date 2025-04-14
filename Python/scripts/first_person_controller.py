#!/usr/bin/env python
"""
First-Person Character Controller Script for Free Company Phase 1 (Days 2-3)
Implements:
- Create a basic first-person character blueprint
- WASD movement
- Jumping functionality
- Basic interaction system
- Sprinting
- Basic collision detection
- Simple camera system with head bobbing
"""

import sys
import os
import socket
import json
import logging
from typing import Dict, Any, Optional, List

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("FirstPersonController")


def send_mcp_command(command: str, params: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Send a command to the Unreal MCP server with automatic socket lifecycle management."""
    sock = None
    try:
        # Create a new socket for each command
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("127.0.0.1", 55557))

        # Create command object
        command_obj = {"type": command, "params": params}

        # Convert to JSON and send
        command_json = json.dumps(command_obj)
        logger.info(f"Sending command: {command_json}")
        sock.sendall(command_json.encode("utf-8"))

        # Receive response
        chunks = []
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            chunks.append(chunk)

            # Try parsing to see if we have a complete response
            try:
                data = b"".join(chunks)
                json.loads(data.decode("utf-8"))
                # If we can parse it, we have the complete response
                break
            except json.JSONDecodeError:
                # Not a complete JSON object yet, continue receiving
                continue

        # Parse response
        data = b"".join(chunks)
        response = json.loads(data.decode("utf-8"))
        logger.info(f"Received response: {response}")
        return response

    except Exception as e:
        logger.error(f"Error in socket communication: {e}")
        return None
    finally:
        # Always close the socket when done
        if sock:
            sock.close()


def create_blueprint(name: str, parent_class: str = "Character") -> bool:
    """Create a blueprint with the given name and parent class."""
    bp_params = {"name": name, "parent_class": parent_class}

    response = send_mcp_command("create_blueprint", bp_params)

    # Check response
    if not response or response.get("status") != "success":
        logger.error(f"Failed to create blueprint: {response}")
        return False

    # Check if blueprint already existed
    if response.get("result", {}).get("already_exists"):
        logger.info(f"Blueprint '{name}' already exists, reusing it")
    else:
        logger.info(f"Blueprint '{name}' created successfully!")

    return True


def add_component(
    blueprint_name: str,
    component_type: str,
    component_name: str,
    location: List[float] = None,
    rotation: List[float] = None,
    scale: List[float] = None,
    properties: Dict[str, Any] = None,
) -> bool:
    """Add a component to the specified blueprint."""
    component_params: Dict[str, Any] = {
        "blueprint_name": blueprint_name,
        "component_type": component_type,
        "component_name": component_name,
    }

    # Add optional parameters if provided
    if location:
        component_params["location"] = location
    if rotation:
        component_params["rotation"] = rotation
    if scale:
        component_params["scale"] = scale
    if properties:
        component_params["component_properties"] = properties

    response = send_mcp_command("add_component_to_blueprint", component_params)

    # Check response
    if not response or response.get("status") != "success":
        logger.error(
            f"Failed to add {component_type} component '{component_name}': {response}"
        )
        return False

    logger.info(
        f"Component '{component_name}' of type '{component_type}' added successfully!"
    )
    return True


def add_variable(
    blueprint_name: str,
    variable_name: str,
    variable_type: str,
    default_value: Any,
    is_exposed: bool = True,
) -> bool:
    """Add a variable to the specified blueprint."""
    params = {
        "blueprint_name": blueprint_name,
        "variable_name": variable_name,
        "variable_type": variable_type,
        "default_value": default_value,
        "is_exposed": is_exposed,
    }

    response = send_mcp_command("add_blueprint_variable", params)

    if not response or response.get("status") != "success":
        logger.error(f"Failed to add variable {variable_name}: {response}")
        return False

    logger.info(f"Variable {variable_name} added successfully!")
    return True


def add_event_node(
    blueprint_name: str, event_type: str, node_position: List[float] = None
) -> Optional[str]:
    """Add an event node to the blueprint."""
    params = {"blueprint_name": blueprint_name, "event_type": event_type}

    if node_position:
        params["node_position"] = node_position

    response = send_mcp_command("add_blueprint_event_node", params)

    if not response or response.get("status") != "success":
        logger.error(f"Failed to add {event_type} event node: {response}")
        return None

    logger.info(f"{event_type} event node added successfully!")
    return response.get("result", {}).get("node_id")


def add_input_action_node(
    blueprint_name: str, action_name: str, node_position: List[float] = None
) -> Optional[str]:
    """Add an input action node to the blueprint."""
    params = {"blueprint_name": blueprint_name, "action_name": action_name}

    if node_position:
        params["node_position"] = node_position

    response = send_mcp_command("add_blueprint_input_action_node", params)

    if not response or response.get("status") != "success":
        logger.error(f"Failed to add input action node for {action_name}: {response}")
        return None

    logger.info(f"Input action node for {action_name} added successfully!")
    return response.get("result", {}).get("node_id")


def add_function_node(
    blueprint_name: str,
    function_name: str,
    target: str = "self",
    params: Dict[str, Any] = None,
    node_position: List[float] = None,
) -> Optional[str]:
    """Add a function node to the blueprint."""
    function_params = {
        "blueprint_name": blueprint_name,
        "function_name": function_name,
        "target": target,
    }

    if params:
        function_params["params"] = params

    if node_position:
        function_params["node_position"] = node_position

    response = send_mcp_command("add_blueprint_function_node", function_params)

    if not response or response.get("status") != "success":
        logger.error(f"Failed to add function node {function_name}: {response}")
        return None

    logger.info(f"Function node {function_name} added successfully!")
    return response.get("result", {}).get("node_id")


def connect_nodes(
    blueprint_name: str,
    source_node_id: str,
    source_pin: str,
    target_node_id: str,
    target_pin: str,
) -> bool:
    """Connect two nodes in the blueprint."""
    params = {
        "blueprint_name": blueprint_name,
        "source_node_id": source_node_id,
        "source_pin": source_pin,
        "target_node_id": target_node_id,
        "target_pin": target_pin,
    }

    response = send_mcp_command("connect_blueprint_nodes", params)

    if not response or response.get("status") != "success":
        logger.error(f"Failed to connect nodes: {response}")
        return False

    logger.info(f"Nodes connected successfully!")
    return True


def compile_blueprint(blueprint_name: str) -> bool:
    """Compile the specified blueprint."""
    compile_params = {"blueprint_name": blueprint_name}

    response = send_mcp_command("compile_blueprint", compile_params)

    if not response or response.get("status") != "success":
        logger.error(f"Failed to compile blueprint '{blueprint_name}': {response}")
        return False

    logger.info(f"Blueprint '{blueprint_name}' compiled successfully!")
    return True


def create_first_person_character():
    """Create the first-person character blueprint."""
    bp_name = "BP_FirstPersonCharacter"

    # Create the character blueprint
    if not create_blueprint(bp_name, "Character"):
        return False

    # Add the first-person camera component
    if not add_component(
        blueprint_name=bp_name,
        component_type="CameraComponent",
        component_name="FirstPersonCamera",
        location=[0.0, 0.0, 90.0],  # At eye level
        properties={"bUsePawnControlRotation": True},
    ):
        return False

    # Add character mesh component
    if not add_component(
        blueprint_name=bp_name,
        component_type="SkeletalMeshComponent",
        component_name="CharacterMesh",
        location=[0.0, 0.0, -90.0],  # Offset downward for proper placement
        properties={"bCastDynamicShadow": True, "bVisible": True},
    ):
        return False

    # Add arms mesh component
    if not add_component(
        blueprint_name=bp_name,
        component_type="SkeletalMeshComponent",
        component_name="ArmsMesh",
        location=[0.0, 0.0, -5.0],  # Slightly below camera
        properties={"bCastDynamicShadow": False, "bOnlyOwnerSee": True},
    ):
        return False

    # Add collision capsule settings (already part of Character class)

    # Add character variables
    variables = [
        ("DefaultWalkSpeed", "Float", 600.0),
        ("SprintMultiplier", "Float", 1.5),
        ("JumpHeight", "Float", 600.0),
        ("HeadBobAmplitude", "Float", 5.0),
        ("HeadBobFrequency", "Float", 8.0),
        ("bIsInteracting", "Boolean", False),
        ("InteractionDistance", "Float", 200.0),
    ]

    for var_name, var_type, default_value in variables:
        if not add_variable(bp_name, var_name, var_type, default_value):
            return False

    # Implement character input and movement logic
    setup_movement_logic(bp_name)

    # Implement head bobbing
    setup_head_bobbing(bp_name)

    # Implement interaction system
    setup_interaction_system(bp_name)

    # Compile the blueprint
    return compile_blueprint(bp_name)


def setup_movement_logic(bp_name: str):
    """Setup the character movement logic."""
    logger.info("Setting up movement logic...")

    # First, we need to handle input actions and axis mappings
    # We'll use the BeginPlay event to set up initial values
    begin_play_id = add_event_node(bp_name, "BeginPlay", [-400, 0])

    # Set character walk speed
    get_movement_comp_id = add_function_node(
        blueprint_name=bp_name,
        function_name="GetCharacterMovement",
        node_position=[-200, 0],
    )

    set_speed_id = add_function_node(
        blueprint_name=bp_name,
        function_name="SetWalkingSpeed",
        target="CharacterMovement",  # Reference to movement component
        params={"WalkSpeed": {"variable": "DefaultWalkSpeed"}},
        node_position=[0, 0],
    )

    # Connect nodes
    connect_nodes(bp_name, begin_play_id, "Then", get_movement_comp_id, "Execute")
    connect_nodes(bp_name, get_movement_comp_id, "ReturnValue", set_speed_id, "self")
    connect_nodes(bp_name, get_movement_comp_id, "Then", set_speed_id, "Execute")

    # Setup axis mappings for movement
    # MoveForward
    move_forward_id = add_event_node(bp_name, "InputAxis", [-400, 100])
    add_movement_input_id = add_function_node(
        blueprint_name=bp_name,
        function_name="AddMovementInput",
        params={
            "WorldDirection": {"function": "GetActorForwardVector"},
            "ScaleValue": {
                "variable": "AxisValue"
            },  # This is provided by the InputAxis event
        },
        node_position=[-100, 100],
    )

    connect_nodes(bp_name, move_forward_id, "Then", add_movement_input_id, "Execute")

    # MoveRight
    move_right_id = add_event_node(bp_name, "InputAxis", [-400, 200])
    add_right_movement_id = add_function_node(
        blueprint_name=bp_name,
        function_name="AddMovementInput",
        params={
            "WorldDirection": {"function": "GetActorRightVector"},
            "ScaleValue": {
                "variable": "AxisValue"
            },  # This is provided by the InputAxis event
        },
        node_position=[-100, 200],
    )

    connect_nodes(bp_name, move_right_id, "Then", add_right_movement_id, "Execute")

    # Setup jump
    jump_id = add_input_action_node(bp_name, "Jump", [-400, 300])
    jump_func_id = add_function_node(
        blueprint_name=bp_name, function_name="Jump", node_position=[-100, 300]
    )

    connect_nodes(bp_name, jump_id, "Pressed", jump_func_id, "Execute")

    # Setup sprint
    sprint_id = add_input_action_node(bp_name, "Sprint", [-400, 400])

    # Sprint start (pressed)
    sprint_start_id = add_function_node(
        blueprint_name=bp_name,
        function_name="GetCharacterMovement",
        node_position=[-200, 400],
    )

    get_default_speed_id = add_function_node(
        blueprint_name=bp_name,
        function_name="GetVarDefaultWalkSpeed",  # Custom function to get variable
        node_position=[-50, 375],
    )

    get_sprint_multi_id = add_function_node(
        blueprint_name=bp_name,
        function_name="GetVarSprintMultiplier",  # Custom function to get variable
        node_position=[-50, 425],
    )

    multiply_id = add_function_node(
        blueprint_name=bp_name,
        function_name="Multiply_FloatFloat",
        params={},  # Will be connected from outputs of previous nodes
        node_position=[150, 400],
    )

    set_sprint_speed_id = add_function_node(
        blueprint_name=bp_name,
        function_name="SetWalkingSpeed",
        target="CharacterMovement",
        params={},  # Will be connected from multiply output
        node_position=[350, 400],
    )

    # Connect sprint pressed nodes
    connect_nodes(bp_name, sprint_id, "Pressed", sprint_start_id, "Execute")
    connect_nodes(bp_name, sprint_start_id, "ReturnValue", set_sprint_speed_id, "self")
    connect_nodes(bp_name, get_default_speed_id, "ReturnValue", multiply_id, "A")
    connect_nodes(bp_name, get_sprint_multi_id, "ReturnValue", multiply_id, "B")
    connect_nodes(bp_name, multiply_id, "ReturnValue", set_sprint_speed_id, "WalkSpeed")
    connect_nodes(bp_name, sprint_start_id, "Then", set_sprint_speed_id, "Execute")

    # Sprint end (released)
    sprint_end_id = add_function_node(
        blueprint_name=bp_name,
        function_name="GetCharacterMovement",
        node_position=[-200, 500],
    )

    set_normal_speed_id = add_function_node(
        blueprint_name=bp_name,
        function_name="SetWalkingSpeed",
        target="CharacterMovement",
        params={"WalkSpeed": {"variable": "DefaultWalkSpeed"}},
        node_position=[0, 500],
    )

    # Connect sprint released nodes
    connect_nodes(bp_name, sprint_id, "Released", sprint_end_id, "Execute")
    connect_nodes(bp_name, sprint_end_id, "ReturnValue", set_normal_speed_id, "self")
    connect_nodes(bp_name, sprint_end_id, "Then", set_normal_speed_id, "Execute")


def setup_head_bobbing(bp_name: str):
    """Setup head bobbing for the camera."""
    logger.info("Setting up head bobbing...")

    # Add tick event to update head bobbing
    tick_id = add_event_node(bp_name, "EventTick", [-400, 600])

    # Check if the character is moving
    get_velocity_id = add_function_node(
        blueprint_name=bp_name, function_name="GetVelocity", node_position=[-200, 600]
    )

    get_velocity_length_id = add_function_node(
        blueprint_name=bp_name,
        function_name="VSize",
        params={},  # Will be connected from GetVelocity
        node_position=[-50, 600],
    )

    branch_id = add_function_node(
        blueprint_name=bp_name,
        function_name="Branch",
        params={
            "Condition": {"function": "GreaterThan_FloatFloat", "params": {"A": 10.0}}
        },  # Check if velocity > 10
        node_position=[100, 600],
    )

    # Get time for bobbing calculation
    get_time_id = add_function_node(
        blueprint_name=bp_name,
        function_name="GetGameTimeInSeconds",
        node_position=[250, 550],
    )

    # Calculate bobbing offset using sin function
    multiply_time_id = add_function_node(
        blueprint_name=bp_name,
        function_name="Multiply_FloatFloat",
        params={"B": {"variable": "HeadBobFrequency"}},
        node_position=[400, 550],
    )

    sin_id = add_function_node(
        blueprint_name=bp_name, function_name="Sin", params={}, node_position=[550, 550]
    )

    multiply_amplitude_id = add_function_node(
        blueprint_name=bp_name,
        function_name="Multiply_FloatFloat",
        params={"B": {"variable": "HeadBobAmplitude"}},
        node_position=[700, 550],
    )

    # Get camera component reference
    get_camera_id = add_function_node(
        blueprint_name=bp_name,
        function_name="GetComponentByName",
        params={"Name": "FirstPersonCamera"},
        node_position=[400, 650],
    )

    # Set camera relative location
    set_rel_location_id = add_function_node(
        blueprint_name=bp_name,
        function_name="SetRelativeLocation",
        target="Component",  # Will be connected from GetComponentByName
        params={
            "NewLocation": {
                "function": "MakeVector",
                "params": {"X": 0.0, "Y": 0.0, "Z": 0.0},
            }
        },  # Z will be connected
        node_position=[700, 650],
    )

    # Connect all head bobbing nodes
    connect_nodes(bp_name, tick_id, "Then", get_velocity_id, "Execute")
    connect_nodes(bp_name, get_velocity_id, "ReturnValue", get_velocity_length_id, "A")
    connect_nodes(
        bp_name, get_velocity_length_id, "ReturnValue", branch_id, "Condition"
    )
    connect_nodes(bp_name, get_velocity_id, "Then", branch_id, "Execute")

    # Connect true branch (apply head bobbing)
    connect_nodes(bp_name, branch_id, "True", get_time_id, "Execute")
    connect_nodes(bp_name, get_time_id, "ReturnValue", multiply_time_id, "A")
    connect_nodes(bp_name, multiply_time_id, "ReturnValue", sin_id, "Value")
    connect_nodes(bp_name, sin_id, "ReturnValue", multiply_amplitude_id, "A")
    connect_nodes(bp_name, get_time_id, "Then", get_camera_id, "Execute")
    connect_nodes(bp_name, get_camera_id, "ReturnValue", set_rel_location_id, "self")
    connect_nodes(
        bp_name,
        multiply_amplitude_id,
        "ReturnValue",
        set_rel_location_id,
        "NewLocation.Z",
    )
    connect_nodes(bp_name, get_camera_id, "Then", set_rel_location_id, "Execute")


def setup_interaction_system(bp_name: str):
    """Setup the basic interaction system."""
    logger.info("Setting up interaction system...")

    # Add input action for interaction
    interact_id = add_input_action_node(bp_name, "Interact", [-400, 800])

    # Perform a line trace to check for interactable objects
    get_camera_id = add_function_node(
        blueprint_name=bp_name,
        function_name="GetComponentByName",
        params={"Name": "FirstPersonCamera"},
        node_position=[-200, 800],
    )

    get_camera_location_id = add_function_node(
        blueprint_name=bp_name,
        function_name="GetWorldLocation",
        target="Component",
        node_position=[-50, 750],
    )

    get_camera_forward_id = add_function_node(
        blueprint_name=bp_name,
        function_name="GetForwardVector",
        target="Component",
        node_position=[-50, 850],
    )

    multiply_range_id = add_function_node(
        blueprint_name=bp_name,
        function_name="Multiply_VectorFloat",
        params={"B": {"variable": "InteractionDistance"}},
        node_position=[100, 850],
    )

    add_vectors_id = add_function_node(
        blueprint_name=bp_name,
        function_name="Add_VectorVector",
        params={},
        node_position=[250, 800],
    )

    line_trace_id = add_function_node(
        blueprint_name=bp_name,
        function_name="LineTraceByChannel",
        params={
            "TraceChannel": "Visibility",
            "bTraceComplex": True,
            "ActorsToIgnore": {"array": [{"self": True}]},
            "bIgnoreSelf": True,
        },
        node_position=[400, 800],
    )

    branch_hit_id = add_function_node(
        blueprint_name=bp_name,
        function_name="Branch",
        params={},
        node_position=[550, 800],
    )

    # Get the hit actor and check if it's interactable (placeholder for now)
    # In a full implementation, we would check for an interface or tag
    print_interact_id = add_function_node(
        blueprint_name=bp_name,
        function_name="PrintString",
        params={"InString": "Interacting with object", "Duration": 2.0},
        node_position=[700, 750],
    )

    # Connect all interaction nodes
    connect_nodes(bp_name, interact_id, "Pressed", get_camera_id, "Execute")
    connect_nodes(bp_name, get_camera_id, "ReturnValue", get_camera_location_id, "self")
    connect_nodes(bp_name, get_camera_id, "ReturnValue", get_camera_forward_id, "self")
    connect_nodes(bp_name, get_camera_id, "Then", get_camera_location_id, "Execute")
    connect_nodes(
        bp_name, get_camera_location_id, "Then", get_camera_forward_id, "Execute"
    )
    connect_nodes(bp_name, get_camera_forward_id, "ReturnValue", multiply_range_id, "A")
    connect_nodes(bp_name, get_camera_location_id, "ReturnValue", add_vectors_id, "A")
    connect_nodes(bp_name, multiply_range_id, "ReturnValue", add_vectors_id, "B")
    connect_nodes(bp_name, get_camera_forward_id, "Then", line_trace_id, "Execute")
    connect_nodes(
        bp_name, get_camera_location_id, "ReturnValue", line_trace_id, "Start"
    )
    connect_nodes(bp_name, add_vectors_id, "ReturnValue", line_trace_id, "End")
    connect_nodes(bp_name, line_trace_id, "bBlockingHit", branch_hit_id, "Condition")
    connect_nodes(bp_name, line_trace_id, "Then", branch_hit_id, "Execute")
    connect_nodes(bp_name, branch_hit_id, "True", print_interact_id, "Execute")


def main():
    """Main function to create the first-person character controller."""
    logger.info("Starting first-person character controller implementation...")

    # Create the character blueprint with all required functionality
    if create_first_person_character():
        logger.info(
            "First-person character controller implementation completed successfully!"
        )
    else:
        logger.error("Failed to implement first-person character controller.")


if __name__ == "__main__":
    main()
