"""
Unreal Engine MCP Server

A simple MCP server for interacting with Unreal Engine.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List, Optional
import uvicorn
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
    handlers=[logging.FileHandler("unreal_mcp.log"), logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("UnrealMCP")

# Initialize FastAPI app
app = FastAPI(title="UnrealMCP", description="Unreal Engine MCP Server")


class MCPCommand(BaseModel):
    command: str
    params: Dict[str, Any] = {}


@app.get("/status")
async def get_status():
    """Get server status."""
    return {"status": "running", "version": "0.1.0"}


@app.post("/command")
async def handle_command(command: MCPCommand):
    """Handle MCP commands."""
    try:
        logger.info(
            f"Received command: {command.command} with params: {command.params}"
        )

        if command.command == "CreateLevel":
            return handle_create_level(command.params)
        elif command.command == "AddActor":
            return handle_add_actor(command.params)
        elif command.command == "SetComponentProperty":
            return handle_set_component_property(command.params)
        elif command.command == "SaveLevel":
            return handle_save_level(command.params)
        elif command.command == "RefreshContentBrowser":
            return handle_refresh_content_browser(command.params)
        elif command.command == "AddBlueprintNode":
            return handle_add_blueprint_node(command.params)
        elif command.command == "AddInputMapping":
            return handle_add_input_mapping(command.params)
        elif command.command == "create_blueprint":
            return handle_create_blueprint(command.params)
        elif command.command == "set_blueprint_property":
            return handle_set_blueprint_property(command.params)
        elif command.command == "SetLevelGameMode":
            return handle_set_level_game_mode(command.params)
        else:
            raise HTTPException(
                status_code=400, detail=f"Unknown command: {command.command}"
            )

    except Exception as e:
        logger.error(f"Error handling command: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


def handle_create_level(params: Dict[str, Any]) -> Dict[str, Any]:
    """Handle creating a new level."""
    try:
        level_name = params.get("levelName")
        template = params.get("template", "EmptyLevel")
        save_path = params.get("savePath", f"/Game/Maps/{level_name}")
        logger.info(
            f"Creating level: {level_name} (template: {template}) at {save_path}"
        )

        # Here we would call the MCPActorManager's CreateLevel function
        # For now, we'll return a mock success response
        return {
            "success": True,
            "message": f"Created level {level_name} with template {template}",
        }
    except Exception as e:
        logger.error(f"Error creating level: {str(e)}")
        return {"success": False, "error": str(e)}


def handle_add_actor(params: Dict[str, Any]) -> Dict[str, Any]:
    """Handle adding an actor to the level."""
    try:
        actor_class = params.get("actorClass")
        actor_name = params.get("actorName")
        location = params.get("location", {"x": 0, "y": 0, "z": 0})
        rotation = params.get("rotation", {"pitch": 0, "yaw": 0, "roll": 0})
        scale = params.get("scale", {"x": 1, "y": 1, "z": 1})
        static_mesh = params.get("staticMesh")

        logger.info(f"Adding actor {actor_name} ({actor_class}) at location {location}")

        # Here we would call the MCPActorManager's AddActor function
        # For now, we'll return a mock success response
        return {
            "success": True,
            "message": f"Added {actor_class} actor named {actor_name}",
        }
    except Exception as e:
        logger.error(f"Error adding actor: {str(e)}")
        return {"success": False, "error": str(e)}


def handle_set_component_property(params: Dict[str, Any]) -> Dict[str, Any]:
    """Handle setting a component property."""
    try:
        blueprint_name = params.get("blueprintName")
        component_name = params.get("componentName")
        property_name = params.get("propertyName")
        property_value = params.get("propertyValue")

        logger.info(
            f"Setting property {property_name} to {property_value} on {component_name} in {blueprint_name}"
        )

        # Here we would call the MCPActorManager's SetComponentProperty function
        # For now, we'll return a mock success response
        return {
            "success": True,
            "message": f"Set {property_name} to {property_value} on {component_name}",
        }
    except Exception as e:
        logger.error(f"Error setting component property: {str(e)}")
        return {"success": False, "error": str(e)}


def handle_save_level(params: Dict[str, Any]) -> Dict[str, Any]:
    """Handle saving the current level."""
    try:
        level_name = params.get("levelName")
        save_path = params.get("savePath", f"/Game/Maps/{level_name}")
        logger.info(f"Saving level {level_name} to {save_path}")

        # Here we would call the MCPActorManager's SaveLevel function
        # For now, we'll return a mock success response
        return {
            "success": True,
            "message": f"Saved level {level_name} to {save_path}",
        }
    except Exception as e:
        logger.error(f"Error saving level: {str(e)}")
        return {"success": False, "error": str(e)}


def handle_refresh_content_browser(params: Dict[str, Any]) -> Dict[str, Any]:
    """Handle refreshing the content browser."""
    try:
        logger.info("Refreshing content browser")

        # Here we would call the MCPActorManager's RefreshContentBrowser function
        # For now, we'll return a mock success response
        return {
            "success": True,
            "message": "Content browser refreshed",
        }
    except Exception as e:
        logger.error(f"Error refreshing content browser: {str(e)}")
        return {"success": False, "error": str(e)}


def handle_add_blueprint_node(params: Dict[str, Any]) -> Dict[str, Any]:
    """Handle adding a node to a blueprint."""
    try:
        blueprint_name = params.get("blueprintName")
        node_type = params.get("nodeType")
        node_name = params.get("nodeName")
        location = params.get("location", [0, 0])
        connections = params.get("connections", {})

        logger.info(
            f"Adding {node_type} node '{node_name}' to blueprint {blueprint_name} at location {location}"
        )

        # Here we would call the MCPBlueprintNodeCommands' AddBlueprintNode function
        # For now, we'll return a mock success response
        return {
            "success": True,
            "message": f"Added {node_type} node '{node_name}' to blueprint {blueprint_name}",
        }
    except Exception as e:
        logger.error(f"Error adding blueprint node: {str(e)}")
        return {"success": False, "error": str(e)}


def handle_add_input_mapping(params: Dict[str, Any]) -> Dict[str, Any]:
    """Handle adding an input mapping."""
    try:
        name = params.get("name")
        mapping_type = params.get("type")
        scale = params.get("scale", 1.0)
        keys = params.get("keys", [])

        logger.info(
            f"Adding {mapping_type} input mapping '{name}' with keys {keys} and scale {scale}"
        )

        # Here we would call the MCPBlueprintNodeCommands' AddInputMapping function
        # For now, we'll return a mock success response
        return {
            "success": True,
            "message": f"Added {mapping_type} input mapping '{name}' with keys {keys}",
        }
    except Exception as e:
        logger.error(f"Error adding input mapping: {str(e)}")
        return {"success": False, "error": str(e)}


def handle_create_blueprint(params: Dict[str, Any]) -> Dict[str, Any]:
    """Handle creating a new blueprint."""
    try:
        name = params.get("name")
        parent_class = params.get("parent_class")

        logger.info(f"Creating blueprint {name} with parent class {parent_class}")

        # Here we would call the MCPBlueprintCommands' CreateBlueprint function
        # For now, we'll return a mock success response
        return {
            "success": True,
            "message": f"Created blueprint {name} with parent class {parent_class}",
        }
    except Exception as e:
        logger.error(f"Error creating blueprint: {str(e)}")
        return {"success": False, "error": str(e)}


def handle_set_blueprint_property(params: Dict[str, Any]) -> Dict[str, Any]:
    """Handle setting a blueprint property."""
    try:
        blueprint_name = params.get("blueprintName")
        property_name = params.get("propertyName")
        property_value = params.get("propertyValue")

        logger.info(
            f"Setting property {property_name} to {property_value} on blueprint {blueprint_name}"
        )

        # Here we would call the MCPBlueprintCommands' SetBlueprintProperty function
        # For now, we'll return a mock success response
        return {
            "success": True,
            "message": f"Set {property_name} to {property_value} on blueprint {blueprint_name}",
        }
    except Exception as e:
        logger.error(f"Error setting blueprint property: {str(e)}")
        return {"success": False, "error": str(e)}


def handle_set_level_game_mode(params: Dict[str, Any]) -> Dict[str, Any]:
    """Handle setting the game mode for a level."""
    try:
        level_name = params.get("levelName")
        game_mode = params.get("gameMode")

        logger.info(f"Setting game mode {game_mode} for level {level_name}")

        # Here we would call the MCPActorManager's SetLevelGameMode function
        # For now, we'll return a mock success response
        return {
            "success": True,
            "message": f"Set game mode {game_mode} for level {level_name}",
        }
    except Exception as e:
        logger.error(f"Error setting level game mode: {str(e)}")
        return {"success": False, "error": str(e)}


if __name__ == "__main__":
    print("Starting Unreal MCP Server...")
    print("Make sure Unreal Editor is running with the UnrealMCP plugin enabled")
    uvicorn.run(app, host="127.0.0.1", port=8000)
