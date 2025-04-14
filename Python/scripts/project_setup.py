#!/usr/bin/env python
"""
Project Setup Script for Free Company Phase 1 (Day 1)
- Creates necessary folders in Content directory
- Sets up basic project settings
- Configures input mappings for WASD, jumping, and interaction
"""

import sys
import os
import socket
import json
import logging
from typing import Dict, Any, Optional

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("ProjectSetup")


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


def create_folder(path: str) -> bool:
    """Create a folder in the content directory."""
    response = send_mcp_command("create_folder", {"path": f"/Game/{path}"})

    if not response or response.get("status") != "success":
        logger.error(f"Failed to create folder {path}: {response}")
        return False

    logger.info(f"Folder '{path}' created successfully!")
    return True


def setup_input_mapping(action_name: str, key: str, input_type: str = "Action") -> bool:
    """Helper function to set up an input mapping."""
    input_params = {"action_name": action_name, "key": key, "input_type": input_type}

    response = send_mcp_command("create_input_mapping", input_params)

    success = (
        response
        and response.get("status") == "success"
        and response.get("result", {}).get("success")
    )

    if success:
        logger.info(f"Input mapping '{action_name}' created with key '{key}'")
    else:
        logger.error(f"Failed to create input mapping: {response}")

    return success


def create_project_structure():
    """Create the necessary folders in Content directory as per the implementation plan."""
    logger.info("Creating project folder structure...")

    # Create necessary folders
    folders = [
        "Characters",
        "Environments",
        "Blueprints",
        "Materials",
        "Meshes",
        "UI",
        "VFX",
        "Blueprints/FirstPerson",
    ]

    for folder in folders:
        create_folder(folder)

    logger.info("Project folder structure creation completed!")


def setup_input_mappings():
    """Configure input mappings for WASD, jumping, and interaction."""
    logger.info("Setting up input mappings...")

    # Movement inputs
    input_mappings = [
        ("MoveForward", "W", "Axis"),
        ("MoveBackward", "S", "Axis"),
        ("MoveRight", "D", "Axis"),
        ("MoveLeft", "A", "Axis"),
        ("Jump", "SpaceBar", "Action"),
        ("Sprint", "LeftShift", "Action"),
        ("Interact", "E", "Action"),
    ]

    for action_name, key, input_type in input_mappings:
        setup_input_mapping(action_name, key, input_type)

    logger.info("Input mappings setup completed!")


def main():
    """Main function to set up the project."""
    logger.info("Starting project setup for Free Company Phase 1...")

    # Create project structure
    create_project_structure()

    # Set up input mappings
    setup_input_mappings()

    logger.info("Project setup completed successfully!")


if __name__ == "__main__":
    main()
