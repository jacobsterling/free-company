#!/usr/bin/env python
"""
Tests for blueprint operations that interact with Unreal Engine.
"""

import pytest
import json
import time
import logging
from pathlib import Path
import sys

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from mcp.scripts.tests.fixtures import send_command, TEST_LEVEL_NAME

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("TestBlueprints")


def test_create_blueprint(test_level):
    """Test creating a blueprint in the test level and verify it exists in Unreal Engine"""
    logger.info(f"Testing blueprint creation in level: {test_level}")

    # Create a test blueprint
    command = {
        "type": "create_blueprint",
        "params": {
            "blueprint_name": "TestBlueprint",
            "parent_class": "Actor",
            "level_name": test_level,
        },
    }

    response = send_command(command)
    assert (
        "error" not in response
    ), f"Failed to create blueprint: {response.get('error')}"
    assert response.get("status") == "success", f"Unexpected response: {response}"

    # Verify the blueprint exists in Unreal Engine
    get_blueprint_command = {
        "type": "get_blueprint_details",
        "params": {"blueprint_name": "TestBlueprint", "level_name": test_level},
    }

    blueprint_response = send_command(get_blueprint_command)
    assert (
        "error" not in blueprint_response
    ), f"Failed to get blueprint details: {blueprint_response.get('error')}"
    assert (
        blueprint_response.get("status") == "success"
    ), f"Unexpected response: {blueprint_response}"

    # Verify the blueprint has the correct parent class
    blueprint_details = blueprint_response.get("blueprint", {})
    assert (
        blueprint_details.get("parent_class") == "Actor"
    ), f"Unexpected parent class: {blueprint_details.get('parent_class')}"

    logger.info("Blueprint creation test passed")


def test_add_component_to_blueprint(test_level):
    """Test adding a component to a blueprint in the test level and verify it exists in Unreal Engine"""
    logger.info(f"Testing adding component to blueprint in level: {test_level}")

    # First, create a test blueprint
    create_command = {
        "type": "create_blueprint",
        "params": {
            "blueprint_name": "ComponentBlueprint",
            "parent_class": "Actor",
            "level_name": test_level,
        },
    }

    create_response = send_command(create_command)
    assert (
        "error" not in create_response
    ), f"Failed to create blueprint: {create_response.get('error')}"

    # Now add a component to the blueprint
    add_component_command = {
        "type": "add_component_to_blueprint",
        "params": {
            "blueprint_name": "ComponentBlueprint",
            "component_class": "StaticMeshComponent",
            "component_name": "TestMeshComponent",
            "level_name": test_level,
        },
    }

    add_component_response = send_command(add_component_command)
    assert (
        "error" not in add_component_response
    ), f"Failed to add component: {add_component_response.get('error')}"
    assert (
        add_component_response.get("status") == "success"
    ), f"Unexpected response: {add_component_response}"

    # Compile the blueprint to apply changes
    compile_command = {
        "type": "compile_blueprint",
        "params": {"blueprint_name": "ComponentBlueprint", "level_name": test_level},
    }

    compile_response = send_command(compile_command)
    assert (
        "error" not in compile_response
    ), f"Failed to compile blueprint: {compile_response.get('error')}"
    assert (
        compile_response.get("status") == "success"
    ), f"Unexpected response: {compile_response}"

    # Verify the component was added by getting the blueprint details
    get_blueprint_command = {
        "type": "get_blueprint_details",
        "params": {"blueprint_name": "ComponentBlueprint", "level_name": test_level},
    }

    blueprint_response = send_command(get_blueprint_command)
    assert (
        "error" not in blueprint_response
    ), f"Failed to get blueprint details: {blueprint_response.get('error')}"

    # Check if our test component is in the list
    blueprint_details = blueprint_response.get("blueprint", {})
    components = blueprint_details.get("components", [])

    test_component_found = False
    for component in components:
        if component.get("name") == "TestMeshComponent":
            test_component_found = True
            assert (
                component.get("class") == "StaticMeshComponent"
            ), f"Unexpected component class: {component.get('class')}"
            break

    assert test_component_found, "Test component not found in blueprint"

    logger.info("Add component to blueprint test passed")


def test_set_component_property(test_level):
    """Test setting a component property in a blueprint in the test level and verify it in Unreal Engine"""
    logger.info(f"Testing setting component property in level: {test_level}")

    # First, create a test blueprint with a component
    create_command = {
        "type": "create_blueprint",
        "params": {
            "blueprint_name": "PropertyBlueprint",
            "parent_class": "Actor",
            "level_name": test_level,
        },
    }

    create_response = send_command(create_command)
    assert (
        "error" not in create_response
    ), f"Failed to create blueprint: {create_response.get('error')}"

    # Add a component to the blueprint
    add_component_command = {
        "type": "add_component_to_blueprint",
        "params": {
            "blueprint_name": "PropertyBlueprint",
            "component_class": "StaticMeshComponent",
            "component_name": "PropertyMeshComponent",
            "level_name": test_level,
        },
    }

    add_component_response = send_command(add_component_command)
    assert (
        "error" not in add_component_response
    ), f"Failed to add component: {add_component_response.get('error')}"

    # Compile the blueprint to apply changes
    compile_command = {
        "type": "compile_blueprint",
        "params": {"blueprint_name": "PropertyBlueprint", "level_name": test_level},
    }

    compile_response = send_command(compile_command)
    assert (
        "error" not in compile_response
    ), f"Failed to compile blueprint: {compile_response.get('error')}"

    # Now set a property on the component
    set_property_command = {
        "type": "set_component_property",
        "params": {
            "blueprint_name": "PropertyBlueprint",
            "component_name": "PropertyMeshComponent",
            "property_name": "Mobility",
            "property_value": "Movable",
            "level_name": test_level,
        },
    }

    set_property_response = send_command(set_property_command)
    assert (
        "error" not in set_property_response
    ), f"Failed to set property: {set_property_response.get('error')}"
    assert (
        set_property_response.get("status") == "success"
    ), f"Unexpected response: {set_property_response}"

    # Compile the blueprint again to apply property changes
    compile_response = send_command(compile_command)
    assert (
        "error" not in compile_response
    ), f"Failed to compile blueprint: {compile_response.get('error')}"

    # Verify the property was set by getting the component properties
    get_property_command = {
        "type": "get_component_property",
        "params": {
            "blueprint_name": "PropertyBlueprint",
            "component_name": "PropertyMeshComponent",
            "property_name": "Mobility",
            "level_name": test_level,
        },
    }

    property_response = send_command(get_property_command)
    assert (
        "error" not in property_response
    ), f"Failed to get property: {property_response.get('error')}"
    assert (
        property_response.get("value") == "Movable"
    ), f"Unexpected property value: {property_response.get('value')}"

    logger.info("Set component property test passed")


def test_spawn_blueprint_actor(test_level):
    """Test spawning an instance of a blueprint in the test level and verify it exists in Unreal Engine"""
    logger.info(f"Testing spawning blueprint actor in level: {test_level}")

    # First, create a test blueprint with a component
    create_command = {
        "type": "create_blueprint",
        "params": {
            "blueprint_name": "SpawnBlueprint",
            "parent_class": "Actor",
            "level_name": test_level,
        },
    }

    create_response = send_command(create_command)
    assert (
        "error" not in create_response
    ), f"Failed to create blueprint: {create_response.get('error')}"

    # Add a component to the blueprint
    add_component_command = {
        "type": "add_component_to_blueprint",
        "params": {
            "blueprint_name": "SpawnBlueprint",
            "component_class": "StaticMeshComponent",
            "component_name": "SpawnMeshComponent",
            "level_name": test_level,
        },
    }

    add_component_response = send_command(add_component_command)
    assert (
        "error" not in add_component_response
    ), f"Failed to add component: {add_component_response.get('error')}"

    # Set the static mesh to a cube
    set_mesh_command = {
        "type": "set_static_mesh_properties",
        "params": {
            "blueprint_name": "SpawnBlueprint",
            "component_name": "SpawnMeshComponent",
            "static_mesh": "/Engine/BasicShapes/Cube.Cube",
            "level_name": test_level,
        },
    }

    set_mesh_response = send_command(set_mesh_command)
    assert (
        "error" not in set_mesh_response
    ), f"Failed to set static mesh: {set_mesh_response.get('error')}"

    # Compile the blueprint to apply changes
    compile_command = {
        "type": "compile_blueprint",
        "params": {"blueprint_name": "SpawnBlueprint", "level_name": test_level},
    }

    compile_response = send_command(compile_command)
    assert (
        "error" not in compile_response
    ), f"Failed to compile blueprint: {compile_response.get('error')}"

    # Now spawn an instance of the blueprint
    spawn_command = {
        "type": "spawn_blueprint_actor",
        "params": {
            "blueprint_name": "SpawnBlueprint",
            "actor_name": "SpawnedActor",
            "location": [100.0, 100.0, 100.0],
            "rotation": [0.0, 0.0, 0.0],
            "scale": [1.0, 1.0, 1.0],
            "level_name": test_level,
        },
    }

    spawn_response = send_command(spawn_command)
    assert (
        "error" not in spawn_response
    ), f"Failed to spawn actor: {spawn_response.get('error')}"
    assert (
        spawn_response.get("status") == "success"
    ), f"Unexpected response: {spawn_response}"

    # Verify the actor exists in the level
    get_actors_command = {
        "type": "get_actors_in_level",
        "params": {"level_name": test_level},
    }

    actors_response = send_command(get_actors_command)
    assert (
        "error" not in actors_response
    ), f"Failed to get actors: {actors_response.get('error')}"

    # Check if our spawned actor is in the list
    test_actor_found = False
    for actor in actors_response.get("actors", []):
        if actor.get("name") == "SpawnedActor":
            test_actor_found = True
            # Verify the actor's location
            location = actor.get("location", {})
            assert (
                abs(location.get("x", 0) - 100.0) < 0.1
            ), f"Unexpected x location: {location.get('x')}"
            assert (
                abs(location.get("y", 0) - 100.0) < 0.1
            ), f"Unexpected y location: {location.get('y')}"
            assert (
                abs(location.get("z", 0) - 100.0) < 0.1
            ), f"Unexpected z location: {location.get('z')}"
            break

    assert test_actor_found, "Spawned actor not found in level"

    logger.info("Spawn blueprint actor test passed")


if __name__ == "__main__":
    pytest.main([__file__])
