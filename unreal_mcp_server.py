"""
Unreal Engine MCP Server

A simple MCP server for interacting with Unreal Engine.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
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

        if command.command == "CreateBlueprint":
            return handle_create_blueprint(command.params)
        elif command.command == "AddComponent":
            return handle_add_component(command.params)
        else:
            raise HTTPException(
                status_code=400, detail=f"Unknown command: {command.command}"
            )

    except Exception as e:
        logger.error(f"Error handling command: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


def handle_create_blueprint(params: Dict[str, Any]) -> Dict[str, Any]:
    """Handle creating a new Blueprint."""
    try:
        name = params.get("name")
        parent_class = params.get("parentClass", "Actor")
        logger.info(f"Creating Blueprint: {name} (parent: {parent_class})")

        # Here you would implement the actual Blueprint creation
        # For now, we'll return a mock success response
        return {
            "success": True,
            "message": f"Created Blueprint {name} with parent class {parent_class}",
        }
    except Exception as e:
        logger.error(f"Error creating Blueprint: {str(e)}")
        return {"success": False, "error": str(e)}


def handle_add_component(params: Dict[str, Any]) -> Dict[str, Any]:
    """Handle adding a component to a Blueprint."""
    try:
        blueprint_name = params.get("blueprintName")
        component_type = params.get("componentType")
        component_name = params.get("componentName")
        logger.info(
            f"Adding component {component_name} ({component_type}) to {blueprint_name}"
        )

        # Here you would implement the actual component addition
        # For now, we'll return a mock success response
        return {
            "success": True,
            "message": f"Added {component_type} component named {component_name} to {blueprint_name}",
        }
    except Exception as e:
        logger.error(f"Error adding component: {str(e)}")
        return {"success": False, "error": str(e)}


if __name__ == "__main__":
    print("Starting Unreal MCP Server...")
    print("Make sure Unreal Editor is running with the UnrealMCP plugin enabled")
    uvicorn.run(app, host="127.0.0.1", port=8000)
