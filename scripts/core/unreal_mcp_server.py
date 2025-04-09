import sys
import os
import json
import socket
import logging
import time
import threading
import signal
from typing import Dict, Any, Optional, List, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("unreal_mcp.log"), logging.StreamHandler()],
)
logger = logging.getLogger("MCP")

# Server settings
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 55557
MAX_CONNECTIONS = 5
BUFFER_SIZE = 4096


class MCPCommand:
    """Base class for MCP commands"""

    def __init__(self, command_type: str, params: Dict[str, Any]):
        self.type = command_type
        self.params = params

    def execute(self) -> Dict[str, Any]:
        """Execute the command and return the response"""
        raise NotImplementedError("Subclasses must implement execute()")


class ActorCommand(MCPCommand):
    """Base class for actor-related commands"""

    def __init__(self, command_type: str, params: Dict[str, Any]):
        super().__init__(command_type, params)
        self.actor_name = params.get("actor_name")
        self.actor_class = params.get("actor_class")
        self.location = params.get("location")
        self.rotation = params.get("rotation")
        self.scale = params.get("scale")


class GetActorsInLevelCommand(ActorCommand):
    def execute(self) -> Dict[str, Any]:
        level_name = self.params.get("level_name")
        # TODO: Implement getting actors in level
        return {"status": "success", "actors": []}


class FindActorsByNameCommand(ActorCommand):
    def execute(self) -> Dict[str, Any]:
        # TODO: Implement finding actors by name
        return {"status": "success", "actors": []}


class CreateActorCommand(ActorCommand):
    def execute(self) -> Dict[str, Any]:
        # TODO: Implement creating actor
        return {"status": "success", "actor_id": "new_actor_id"}


class DeleteActorCommand(ActorCommand):
    def execute(self) -> Dict[str, Any]:
        # TODO: Implement deleting actor
        return {"status": "success"}


class SetActorTransformCommand(ActorCommand):
    def execute(self) -> Dict[str, Any]:
        # TODO: Implement setting actor transform
        return {"status": "success"}


class GetActorPropertiesCommand(ActorCommand):
    def execute(self) -> Dict[str, Any]:
        # TODO: Implement getting actor properties
        return {"status": "success", "properties": {}}


class AddActorCommand(ActorCommand):
    def execute(self) -> Dict[str, Any]:
        # TODO: Implement adding actor
        return {"status": "success", "actor_id": "new_actor_id"}


class EditorCommand(MCPCommand):
    """Base class for editor-related commands"""

    def __init__(self, command_type: str, params: Dict[str, Any]):
        super().__init__(command_type, params)


class FocusViewportCommand(EditorCommand):
    def execute(self) -> Dict[str, Any]:
        location = self.params.get("location")
        # TODO: Implement focusing viewport
        return {"status": "success"}


class TakeScreenshotCommand(EditorCommand):
    def execute(self) -> Dict[str, Any]:
        filename = self.params.get("filename")
        # TODO: Implement taking screenshot
        return {"status": "success"}


class CreateLevelCommand(EditorCommand):
    def execute(self) -> Dict[str, Any]:
        level_name = self.params.get("levelName")
        template = self.params.get("template", "EmptyLevel")
        save_path = self.params.get("savePath")
        # TODO: Implement creating level
        return {"status": "success"}


class SaveLevelCommand(EditorCommand):
    def execute(self) -> Dict[str, Any]:
        level_name = self.params.get("levelName")
        save_path = self.params.get("savePath")
        # TODO: Implement saving level
        return {"status": "success"}


class RefreshContentBrowserCommand(EditorCommand):
    def execute(self) -> Dict[str, Any]:
        # TODO: Implement refreshing content browser
        return {"status": "success"}


class BlueprintCommand(MCPCommand):
    """Base class for blueprint-related commands"""

    def __init__(self, command_type: str, params: Dict[str, Any]):
        super().__init__(command_type, params)
        self.blueprint_name = params.get("blueprint_name")


class CreateBlueprintCommand(BlueprintCommand):
    def execute(self) -> Dict[str, Any]:
        name = self.params.get("name")
        parent_class = self.params.get("parent_class")
        path = self.params.get("path", "/Game/Content/Blueprints")
        # TODO: Implement creating blueprint
        return {"status": "success"}


class AddComponentToBlueprintCommand(BlueprintCommand):
    def execute(self) -> Dict[str, Any]:
        component_class = self.params.get("component_class")
        component_name = self.params.get("component_name")
        # TODO: Implement adding component to blueprint
        return {"status": "success"}


class SetComponentPropertyCommand(BlueprintCommand):
    def execute(self) -> Dict[str, Any]:
        component_name = self.params.get("component_name")
        property_name = self.params.get("property_name")
        property_value = self.params.get("property_value")
        # TODO: Implement setting component property
        return {"status": "success"}


class SetPhysicsPropertiesCommand(BlueprintCommand):
    def execute(self) -> Dict[str, Any]:
        component_name = self.params.get("component_name")
        properties = self.params.get("properties")
        # TODO: Implement setting physics properties
        return {"status": "success"}


class CompileBlueprintCommand(BlueprintCommand):
    def execute(self) -> Dict[str, Any]:
        # TODO: Implement compiling blueprint
        return {"status": "success"}


class SpawnBlueprintActorCommand(BlueprintCommand):
    def execute(self) -> Dict[str, Any]:
        location = self.params.get("location")
        rotation = self.params.get("rotation")
        scale = self.params.get("scale")
        name = self.params.get("name")
        # TODO: Implement spawning blueprint actor
        return {"status": "success", "actor_id": "new_actor_id"}


class SetBlueprintPropertyCommand(BlueprintCommand):
    def execute(self) -> Dict[str, Any]:
        property_name = self.params.get("property_name")
        property_value = self.params.get("property_value")
        # TODO: Implement setting blueprint property
        return {"status": "success"}


class SetStaticMeshPropertiesCommand(BlueprintCommand):
    def execute(self) -> Dict[str, Any]:
        component_name = self.params.get("component_name")
        properties = self.params.get("properties")
        # TODO: Implement setting static mesh properties
        return {"status": "success"}


class BlueprintNodeCommand(MCPCommand):
    """Base class for blueprint node-related commands"""

    def __init__(self, command_type: str, params: Dict[str, Any]):
        super().__init__(command_type, params)
        self.blueprint_name = params.get("blueprintName")


class ConnectBlueprintNodesCommand(BlueprintNodeCommand):
    def execute(self) -> Dict[str, Any]:
        source_node = self.params.get("source_node")
        target_node = self.params.get("target_node")
        source_pin = self.params.get("source_pin")
        target_pin = self.params.get("target_pin")
        # TODO: Implement connecting blueprint nodes
        return {"status": "success"}


class AddInputMappingCommand(BlueprintNodeCommand):
    def execute(self) -> Dict[str, Any]:
        name = self.params.get("name")
        positive_key = self.params.get("positive_key")
        negative_key = self.params.get("negative_key")
        scale = self.params.get("scale", 1.0)
        # TODO: Implement adding input mapping
        return {"status": "success"}


class AddBlueprintNodeCommand(BlueprintNodeCommand):
    def execute(self) -> Dict[str, Any]:
        node_type = self.params.get("nodeType")
        node_name = self.params.get("nodeName")
        location = self.params.get("location")
        connections = self.params.get("connections")
        # TODO: Implement adding blueprint node
        return {"status": "success"}


class GameCommand(MCPCommand):
    """Base class for game-related commands"""

    def __init__(self, command_type: str, params: Dict[str, Any]):
        super().__init__(command_type, params)


class SetLevelGameModeCommand(GameCommand):
    def execute(self) -> Dict[str, Any]:
        level_name = self.params.get("levelName")
        game_mode = self.params.get("gameMode")
        # TODO: Implement setting level game mode
        return {"status": "success"}


class MCPServer:
    """Main MCP server class"""

    def __init__(self, host: str = DEFAULT_HOST, port: int = DEFAULT_PORT):
        self.host = host
        self.port = port
        self.server_socket = None
        self.running = False
        self.command_handlers = {
            # Actor commands
            "get_actors_in_level": GetActorsInLevelCommand,
            "find_actors_by_name": FindActorsByNameCommand,
            "create_actor": CreateActorCommand,
            "delete_actor": DeleteActorCommand,
            "set_actor_transform": SetActorTransformCommand,
            "get_actor_properties": GetActorPropertiesCommand,
            "AddActor": AddActorCommand,
            # Editor commands
            "focus_viewport": FocusViewportCommand,
            "take_screenshot": TakeScreenshotCommand,
            "CreateLevel": CreateLevelCommand,
            "SaveLevel": SaveLevelCommand,
            "RefreshContentBrowser": RefreshContentBrowserCommand,
            # Blueprint commands
            "create_blueprint": CreateBlueprintCommand,
            "add_component_to_blueprint": AddComponentToBlueprintCommand,
            "set_component_property": SetComponentPropertyCommand,
            "set_physics_properties": SetPhysicsPropertiesCommand,
            "compile_blueprint": CompileBlueprintCommand,
            "spawn_blueprint_actor": SpawnBlueprintActorCommand,
            "set_blueprint_property": SetBlueprintPropertyCommand,
            "set_static_mesh_properties": SetStaticMeshPropertiesCommand,
            # Blueprint node commands
            "connect_blueprint_nodes": ConnectBlueprintNodesCommand,
            "create_input_mapping": AddInputMappingCommand,
            "AddBlueprintNode": AddBlueprintNodeCommand,
            "AddInputMapping": AddInputMappingCommand,
            # Game commands
            "SetLevelGameMode": SetLevelGameModeCommand,
        }

    def start(self):
        """Start the MCP server"""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(MAX_CONNECTIONS)
            self.running = True

            logger.info(f"MCP server started on {self.host}:{self.port}")

            while self.running:
                try:
                    client_socket, address = self.server_socket.accept()
                    logger.info(f"New connection from {address}")

                    # Handle client in a new thread
                    client_thread = threading.Thread(
                        target=self.handle_client, args=(client_socket,)
                    )
                    client_thread.daemon = True
                    client_thread.start()

                except socket.error as e:
                    if self.running:
                        logger.error(f"Socket error: {str(e)}")
                    break

        except Exception as e:
            logger.error(f"Error starting server: {str(e)}")
        finally:
            self.stop()

    def stop(self):
        """Stop the MCP server"""
        self.running = False
        if self.server_socket:
            self.server_socket.close()
            self.server_socket = None
        logger.info("MCP server stopped")

    def handle_client(self, client_socket: socket.socket):
        """Handle a client connection"""
        try:
            while self.running:
                # Receive command
                data = client_socket.recv(BUFFER_SIZE)
                if not data:
                    break

                try:
                    command = json.loads(data.decode("utf-8"))
                    logger.debug(f"Received command: {command}")

                    # Execute command
                    response = self.execute_command(command)

                    # Send response
                    client_socket.sendall(json.dumps(response).encode("utf-8"))

                except json.JSONDecodeError as e:
                    logger.error(f"Error decoding command: {str(e)}")
                    response = {"status": "error", "message": "Invalid command format"}
                    client_socket.sendall(json.dumps(response).encode("utf-8"))

        except Exception as e:
            logger.error(f"Error handling client: {str(e)}")
        finally:
            client_socket.close()

    def execute_command(self, command: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a command and return the response"""
        try:
            command_type = command.get("type")
            params = command.get("params", {})

            if command_type not in self.command_handlers:
                return {
                    "status": "error",
                    "message": f"Unknown command type: {command_type}",
                }

            command_handler = self.command_handlers[command_type]
            command_instance = command_handler(command_type, params)
            return command_instance.execute()

        except Exception as e:
            logger.error(f"Error executing command: {str(e)}")
            return {"status": "error", "message": str(e)}


def main():
    """Main entry point"""
    # Parse command line arguments
    import argparse

    parser = argparse.ArgumentParser(description="Unreal MCP Server")
    parser.add_argument("--host", default=DEFAULT_HOST, help="Host to bind to")
    parser.add_argument(
        "--port", type=int, default=DEFAULT_PORT, help="Port to bind to"
    )
    args = parser.parse_args()

    # Create and start server
    server = MCPServer(args.host, args.port)

    # Handle Ctrl+C gracefully
    def signal_handler(signum, frame):
        logger.info("Received shutdown signal")
        server.stop()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Start server
    server.start()


if __name__ == "__main__":
    main()
