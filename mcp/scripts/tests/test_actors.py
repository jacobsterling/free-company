#!/usr/bin/env python
"""
Tests for actor operations that interact with Unreal Engine.
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
logger = logging.getLogger("TestActors")


def test_create_actor(test_level):
    """Test creating an actor in the test level and verify it exists in Unreal Engine"""
    logger.info(f"Testing actor creation in level: {test_level}")

    # Create a test actor
    command = {
        "type": "create_actor",
        "params": {
            "actor_class": "StaticMeshActor",
            "actor_name": "TestActor",
            "level_name": test_level,
            "location": {"x": 0, "y": 0, "z": 0},
            "rotation": {"pitch": 0, "yaw": 0, "roll": 0},
            "scale": {"x": 1, "y": 1, "z": 1},
        },
    }

    response = send_command(command)
    assert "error" not in response, f"Failed to create actor: {response.get('error')}"
    assert response.get("status") == "success", f"Unexpected response: {response}"

    # Verify the actor exists in Unreal Engine
    get_actors_command = {
        "type": "get_actors_in_level",
        "params": {"level_name": test_level},
    }

    actors_response = send_command(get_actors_command)
    assert (
        "error" not in actors_response
    ), f"Failed to get actors: {actors_response.get('error')}"
    assert "actors" in actors_response, f"Unexpected response: {actors_response}"

    # Check if our test actor is in the list
    test_actor_found = False
    for actor in actors_response["actors"]:
        if actor["name"] == "TestActor":
            test_actor_found = True
            # Verify the actor's class
            assert (
                actor.get("class") == "StaticMeshActor"
            ), f"Unexpected actor class: {actor.get('class')}"
            # Verify the actor's location
            location = actor.get("location", {})
            assert (
                abs(location.get("x", 0)) < 0.1
            ), f"Unexpected x location: {location.get('x')}"
            assert (
                abs(location.get("y", 0)) < 0.1
            ), f"Unexpected y location: {location.get('y')}"
            assert (
                abs(location.get("z", 0)) < 0.1
            ), f"Unexpected z location: {location.get('z')}"
            break

    assert test_actor_found, "Test actor not found in level"

    logger.info("Actor creation test passed")


def test_delete_actor(test_level):
    """Test deleting an actor from the test level and verify it's removed from Unreal Engine"""
    logger.info(f"Testing actor deletion in level: {test_level}")

    # First, create a test actor
    create_command = {
        "type": "create_actor",
        "params": {
            "actor_class": "StaticMeshActor",
            "actor_name": "ActorToDelete",
            "level_name": test_level,
            "location": {"x": 0, "y": 0, "z": 0},
            "rotation": {"pitch": 0, "yaw": 0, "roll": 0},
            "scale": {"x": 1, "y": 1, "z": 1},
        },
    }

    create_response = send_command(create_command)
    assert (
        "error" not in create_response
    ), f"Failed to create actor: {create_response.get('error')}"

    # Verify the actor was created
    get_actors_command = {
        "type": "get_actors_in_level",
        "params": {"level_name": test_level},
    }

    actors_response = send_command(get_actors_command)
    assert (
        "error" not in actors_response
    ), f"Failed to get actors: {actors_response.get('error')}"

    # Check if our test actor is in the list
    actor_exists = False
    for actor in actors_response.get("actors", []):
        if actor["name"] == "ActorToDelete":
            actor_exists = True
            break

    assert actor_exists, "Test actor not found after creation"

    # Now delete the actor
    delete_command = {
        "type": "delete_actor",
        "params": {"actor_name": "ActorToDelete", "level_name": test_level},
    }

    delete_response = send_command(delete_command)
    assert (
        "error" not in delete_response
    ), f"Failed to delete actor: {delete_response.get('error')}"
    assert (
        delete_response.get("status") == "success"
    ), f"Unexpected response: {delete_response}"

    # Verify the actor is gone from Unreal Engine
    actors_response = send_command(get_actors_command)
    assert (
        "error" not in actors_response
    ), f"Failed to get actors: {actors_response.get('error')}"

    # Check that our test actor is not in the list
    actor_still_exists = False
    for actor in actors_response.get("actors", []):
        if actor["name"] == "ActorToDelete":
            actor_still_exists = True
            break

    assert not actor_still_exists, "Actor still exists after deletion"

    logger.info("Actor deletion test passed")


def test_set_actor_transform(test_level):
    """Test setting an actor's transform in the test level and verify it in Unreal Engine"""
    logger.info(f"Testing actor transform in level: {test_level}")

    # First, create a test actor
    create_command = {
        "type": "create_actor",
        "params": {
            "actor_class": "StaticMeshActor",
            "actor_name": "TransformActor",
            "level_name": test_level,
            "location": {"x": 0, "y": 0, "z": 0},
            "rotation": {"pitch": 0, "yaw": 0, "roll": 0},
            "scale": {"x": 1, "y": 1, "z": 1},
        },
    }

    create_response = send_command(create_command)
    assert (
        "error" not in create_response
    ), f"Failed to create actor: {create_response.get('error')}"

    # Now set the actor's transform
    transform_command = {
        "type": "set_actor_transform",
        "params": {
            "actor_name": "TransformActor",
            "level_name": test_level,
            "location": {"x": 100, "y": 200, "z": 300},
            "rotation": {"pitch": 45, "yaw": 90, "roll": 180},
            "scale": {"x": 2, "y": 3, "z": 4},
        },
    }

    transform_response = send_command(transform_command)
    assert (
        "error" not in transform_response
    ), f"Failed to set actor transform: {transform_response.get('error')}"
    assert (
        transform_response.get("status") == "success"
    ), f"Unexpected response: {transform_response}"

    # Verify the actor's transform was updated in Unreal Engine
    get_actor_command = {
        "type": "get_actor_properties",
        "params": {"actor_name": "TransformActor", "level_name": test_level},
    }

    actor_response = send_command(get_actor_command)
    assert (
        "error" not in actor_response
    ), f"Failed to get actor properties: {actor_response.get('error')}"

    # Check the transform values
    location = actor_response.get("properties", {}).get("location", {})
    assert (
        abs(location.get("x", 0) - 100) < 0.1
    ), f"Unexpected x location: {location.get('x')}"
    assert (
        abs(location.get("y", 0) - 200) < 0.1
    ), f"Unexpected y location: {location.get('y')}"
    assert (
        abs(location.get("z", 0) - 300) < 0.1
    ), f"Unexpected z location: {location.get('z')}"

    rotation = actor_response.get("properties", {}).get("rotation", {})
    assert (
        abs(rotation.get("pitch", 0) - 45) < 0.1
    ), f"Unexpected pitch: {rotation.get('pitch')}"
    assert (
        abs(rotation.get("yaw", 0) - 90) < 0.1
    ), f"Unexpected yaw: {rotation.get('yaw')}"
    assert (
        abs(rotation.get("roll", 0) - 180) < 0.1
    ), f"Unexpected roll: {rotation.get('roll')}"

    scale = actor_response.get("properties", {}).get("scale", {})
    assert abs(scale.get("x", 0) - 2) < 0.1, f"Unexpected x scale: {scale.get('x')}"
    assert abs(scale.get("y", 0) - 3) < 0.1, f"Unexpected y scale: {scale.get('y')}"
    assert abs(scale.get("z", 0) - 4) < 0.1, f"Unexpected z scale: {scale.get('z')}"

    logger.info("Actor transform test passed")


def test_set_actor_property(test_level):
    """Test setting an actor's property in the test level and verify it in Unreal Engine"""
    logger.info(f"Testing actor property in level: {test_level}")

    # First, create a test actor
    create_command = {
        "type": "create_actor",
        "params": {
            "actor_class": "StaticMeshActor",
            "actor_name": "PropertyActor",
            "level_name": test_level,
            "location": {"x": 0, "y": 0, "z": 0},
            "rotation": {"pitch": 0, "yaw": 0, "roll": 0},
            "scale": {"x": 1, "y": 1, "z": 1},
        },
    }

    create_response = send_command(create_command)
    assert (
        "error" not in create_response
    ), f"Failed to create actor: {create_response.get('error')}"

    # Now set a property on the actor
    set_property_command = {
        "type": "set_actor_property",
        "params": {
            "actor_name": "PropertyActor",
            "level_name": test_level,
            "property_name": "bHidden",
            "property_value": True,
        },
    }

    set_property_response = send_command(set_property_command)
    assert (
        "error" not in set_property_response
    ), f"Failed to set actor property: {set_property_response.get('error')}"
    assert (
        set_property_response.get("status") == "success"
    ), f"Unexpected response: {set_property_response}"

    # Verify the property was set in Unreal Engine
    get_property_command = {
        "type": "get_actor_property",
        "params": {
            "actor_name": "PropertyActor",
            "level_name": test_level,
            "property_name": "bHidden",
        },
    }

    property_response = send_command(get_property_command)
    assert (
        "error" not in property_response
    ), f"Failed to get actor property: {property_response.get('error')}"
    assert (
        property_response.get("value") is True
    ), f"Unexpected property value: {property_response.get('value')}"

    logger.info("Actor property test passed")


if __name__ == "__main__":
    pytest.main([__file__])
