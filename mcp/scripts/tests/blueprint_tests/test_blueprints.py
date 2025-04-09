#!/usr/bin/env python
"""
Tests for blueprint operations that interact with Unreal Engine.
"""

import pytest
import json
import time
import os
import logging
from pathlib import Path
import sys

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from mcp.scripts.tests.test_fixtures import send_command, TEST_LEVEL_NAME

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("BlueprintTests")


@pytest.fixture(scope="function")
def test_level():
    """
    Fixture that provides a test level for blueprint operations.
    Creates a new level before each test and cleans it up after.
    """
    logger.info(f"Setting up test level: {TEST_LEVEL_NAME}")

    # Create a new level for testing
    create_level_command = {
        "type": "create_level",
        "params": {"level_name": TEST_LEVEL_NAME},
    }

    response = send_command(create_level_command)
    assert (
        "error" not in response
    ), f"Failed to create test level: {response.get('error')}"

    # Make sure the level is loaded
    load_level_command = {
        "type": "load_level",
        "params": {"level_name": TEST_LEVEL_NAME},
    }

    response = send_command(load_level_command)
    assert (
        "error" not in response
    ), f"Failed to load test level: {response.get('error')}"

    yield TEST_LEVEL_NAME

    # Clean up after the test
    logger.info(f"Cleaning up test level: {TEST_LEVEL_NAME}")

    # Delete the test level
    delete_level_command = {
        "type": "delete_level",
        "params": {"level_name": TEST_LEVEL_NAME},
    }

    response = send_command(delete_level_command)
    if "error" in response:
        logger.warning(f"Failed to delete test level: {response.get('error')}")


def test_create_blueprint(test_level):
    """Test creating a new blueprint and verify it exists."""
    logger.info("Testing blueprint creation")

    blueprint_name = "TestBlueprint"
    parent_class = "Actor"

    # Create the blueprint
    create_command = {
        "type": "create_blueprint",
        "params": {
            "blueprint_name": blueprint_name,
            "parent_class": parent_class,
            "folder_path": "/Game/Tests",
        },
    }

    response = send_command(create_command)
    assert (
        "error" not in response
    ), f"Failed to create blueprint: {response.get('error')}"

    # Verify the blueprint exists
    verify_command = {
        "type": "get_blueprint_info",
        "params": {"blueprint_name": blueprint_name},
    }

    response = send_command(verify_command)
    assert (
        "error" not in response
    ), f"Failed to verify blueprint: {response.get('error')}"
    assert (
        response["parent_class"] == parent_class
    ), f"Blueprint has wrong parent class: {response['parent_class']}"


def test_add_component_to_blueprint(test_level):
    """Test adding a component to a blueprint and verify it was added."""
    logger.info("Testing component addition to blueprint")

    blueprint_name = "ComponentBlueprint"
    component_name = "TestMeshComponent"
    component_type = "StaticMeshComponent"

    # Create the blueprint first
    create_command = {
        "type": "create_blueprint",
        "params": {
            "blueprint_name": blueprint_name,
            "parent_class": "Actor",
            "folder_path": "/Game/Tests",
        },
    }

    response = send_command(create_command)
    assert (
        "error" not in response
    ), f"Failed to create blueprint: {response.get('error')}"

    # Add the component
    add_component_command = {
        "type": "add_component_to_blueprint",
        "params": {
            "blueprint_name": blueprint_name,
            "component_name": component_name,
            "component_type": component_type,
        },
    }

    response = send_command(add_component_command)
    assert "error" not in response, f"Failed to add component: {response.get('error')}"

    # Compile the blueprint
    compile_command = {
        "type": "compile_blueprint",
        "params": {"blueprint_name": blueprint_name},
    }

    response = send_command(compile_command)
    assert (
        "error" not in response
    ), f"Failed to compile blueprint: {response.get('error')}"

    # Verify the component exists
    verify_command = {
        "type": "get_blueprint_components",
        "params": {"blueprint_name": blueprint_name},
    }

    response = send_command(verify_command)
    assert (
        "error" not in response
    ), f"Failed to verify components: {response.get('error')}"
    assert component_name in [
        comp["name"] for comp in response["components"]
    ], f"Component {component_name} not found in blueprint"


def test_set_component_property(test_level):
    """Test setting a property on a blueprint component."""
    logger.info("Testing setting component property")

    blueprint_name = "PropertyBlueprint"
    component_name = "PropertyMeshComponent"

    # Create blueprint and add component
    create_command = {
        "type": "create_blueprint",
        "params": {
            "blueprint_name": blueprint_name,
            "parent_class": "Actor",
            "folder_path": "/Game/Tests",
        },
    }

    response = send_command(create_command)
    assert (
        "error" not in response
    ), f"Failed to create blueprint: {response.get('error')}"

    add_component_command = {
        "type": "add_component_to_blueprint",
        "params": {
            "blueprint_name": blueprint_name,
            "component_name": component_name,
            "component_type": "StaticMeshComponent",
        },
    }

    response = send_command(add_component_command)
    assert "error" not in response, f"Failed to add component: {response.get('error')}"

    # Set the property
    set_property_command = {
        "type": "set_component_property",
        "params": {
            "blueprint_name": blueprint_name,
            "component_name": component_name,
            "property_name": "Mobility",
            "property_value": "Movable",
        },
    }

    response = send_command(set_property_command)
    assert "error" not in response, f"Failed to set property: {response.get('error')}"

    # Verify the property was set
    verify_command = {
        "type": "get_component_property",
        "params": {
            "blueprint_name": blueprint_name,
            "component_name": component_name,
            "property_name": "Mobility",
        },
    }

    response = send_command(verify_command)
    assert (
        "error" not in response
    ), f"Failed to verify property: {response.get('error')}"
    assert (
        response["value"] == "Movable"
    ), f"Property value incorrect: {response['value']}"


def test_spawn_blueprint_actor(test_level):
    """Test spawning a blueprint actor in the level."""
    logger.info("Testing blueprint actor spawning")

    blueprint_name = "SpawnBlueprint"
    spawn_location = {"x": 100.0, "y": 200.0, "z": 300.0}

    # Create the blueprint
    create_command = {
        "type": "create_blueprint",
        "params": {
            "blueprint_name": blueprint_name,
            "parent_class": "Actor",
            "folder_path": "/Game/Tests",
        },
    }

    response = send_command(create_command)
    assert (
        "error" not in response
    ), f"Failed to create blueprint: {response.get('error')}"

    # Spawn the actor
    spawn_command = {
        "type": "spawn_actor",
        "params": {
            "blueprint_name": blueprint_name,
            "location": spawn_location,
            "level_name": test_level,
        },
    }

    response = send_command(spawn_command)
    assert "error" not in response, f"Failed to spawn actor: {response.get('error')}"
    actor_id = response["actor_id"]

    # Verify the actor exists at the correct location
    verify_command = {"type": "get_actor_info", "params": {"actor_id": actor_id}}

    response = send_command(verify_command)
    assert "error" not in response, f"Failed to verify actor: {response.get('error')}"
    assert (
        response["location"] == spawn_location
    ), f"Actor not at correct location: {response['location']}"


if __name__ == "__main__":
    pytest.main([__file__])
