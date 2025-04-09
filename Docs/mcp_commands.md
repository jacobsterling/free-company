# MCP Commands for Free Company Game Development

## Overview
This document outlines the MCP (Model-Controller-Protocol) commands that can be used to create and manipulate objects in the Free Company game. These commands will help automate the creation of game elements, including characters, enemies, effects, and environments.

## File Structure
```
Source/UnrealMCP/
├── Public/
│   ├── UnrealMCPBridge.h
│   └── Commands/
│       ├── UnrealMCPActorCommands.h
│       ├── UnrealMCPEditorCommands.h
│       ├── UnrealMCPBlueprintCommands.h
│       ├── UnrealMCPBlueprintNodeCommands.h
│       ├── UnrealMCPGameCommands.h
│       └── UnrealMCPCommonUtils.h  
├── Private/
│   ├── UnrealMCPBridge.cpp
│   └── Commands/
│       ├── UnrealMCPActorCommands.cpp
│       ├── UnrealMCPEditorCommands.cpp
│       ├── UnrealMCPBlueprintCommands.cpp
│       ├── UnrealMCPBlueprintNodeCommands.cpp
│       ├── UnrealMCPGameCommands.cpp
│       └── UnrealMCPCommonUtils.cpp
```

## Implementation Steps

### Step 1: Set Up Structure (5 min)
- Create `Commands` folders in Public and Private
- Create all header and implementation files

### Step 2: Implement Common Utils (5 min)
- Move all utility methods from `UnrealMCPBridge.cpp` to `UnrealMCPCommonUtils.cpp`
- Actor utilities: `ActorToJson`, `ActorToJsonObject`
- Blueprint utilities: `FindBlueprint`, `FindBlueprintByName`, `FindOrCreateEventGraph`
- Blueprint node utilities: All node creation and connection methods
- JSON utilities: `GetIntArrayFromJson` and other parsing helpers

### Step 3: Implement Command Handlers (10 min)
- Cut & paste each command handler from `UnrealMCPBridge.cpp` to the appropriate implementation file
- For each handler method that uses utility functions, modify to use `FUnrealMCPCommonUtils` instead
- Update the top-level `HandleCommand` in each implementation to route to the appropriate handler

### Step 4: Modify UnrealMCPBridge (10 min)
- Update header file with new member variables
- Add includes for new handler classes
- Initialize command handlers in `Initialize`
- Replace command handling in `ExecuteCommand` with delegation to handlers
- Remove all command handler methods and utility methods that have been moved

## Command Distribution

### FUnrealMCPActorCommands:
- `get_actors_in_level`
- `find_actors_by_name`
- `create_actor`
- `delete_actor`
- `set_actor_transform`
- `get_actor_properties`
- `AddActor`

### FUnrealMCPEditorCommands:
- `focus_viewport`
- `take_screenshot`
- `CreateLevel`
- `SaveLevel`
- `RefreshContentBrowser`

### FUnrealMCPBlueprintCommands:
- `create_blueprint`
- `add_component_to_blueprint`
- `set_component_property`
- `set_physics_properties`
- `compile_blueprint`
- `spawn_blueprint_actor`
- `set_blueprint_property`
- `set_static_mesh_properties`

### FUnrealMCPBlueprintNodeCommands:
- `connect_blueprint_nodes`
- `create_input_mapping`
- `add_blueprint_get_self_component_reference`
- `add_blueprint_self_reference`
- `find_blueprint_nodes`
- `add_blueprint_event_node`
- `add_blueprint_input_action_node`
- `add_blueprint_function_node`
- `add_blueprint_get_component_node`
- `add_blueprint_variable`
- `AddBlueprintNode`
- `AddInputMapping`

### FUnrealMCPGameCommands:
- `create_character_class`
- `create_character_instance`
- `create_enemy_type`
- `create_enemy_instance`
- `create_effect_type`
- `create_effect_instance`
- `create_dungeon_type`
- `create_dungeon_instance`
- `create_boss_type`
- `create_boss_instance`
- `create_vampire_character`
- `create_vampire_enemy`
- `create_blood_effect`
- `create_vampire_castle`
- `create_vampire_lord`

## Utility Methods in UnrealMCPCommonUtils

### Actor Utilities
- `ActorToJson`
- `ActorToJsonObject`

### Blueprint Utilities
- `FindBlueprint`
- `FindBlueprintByName`
- `FindOrCreateEventGraph`

### Blueprint Node Utilities
- `CreateEventNode`
- `CreateFunctionCallNode`
- `CreateVariableGetNode`
- `CreateVariableSetNode`
- `CreateInputActionNode`
- `CreateSelfReferenceNode`
- `ConnectGraphNodes`
- `FindPin`

### JSON Utilities
- `GetIntArrayFromJson`
- `GetFloatArrayFromJson`
- `GetVector2DFromJson`
- `GetVectorFromJson`
- `GetRotatorFromJson`
- `CreateErrorResponse`
- `CreateSuccessResponse`

## Game-Specific Commands

### Character System Commands

#### Create Character Class
```json
{
  "command": "create_character_class",
  "params": {
    "class_name": "Warrior",
    "base_stats": {
      "health": 100,
      "stamina": 100,
      "strength": 10,
      "dexterity": 5,
      "intelligence": 3,
      "willpower": 7
    },
    "resistances": {
      "physical": 0.7,
      "magical": 0.3,
      "mental": 0.4
    },
    "abilities": [
      "Heavy Strike",
      "Defensive Stance",
      "Battle Cry"
    ],
    "settlement_roles": [
      "Blacksmith",
      "Guard"
    ]
  }
}
```

#### Create Character Instance
```json
{
  "command": "create_character_instance",
  "params": {
    "class_name": "Warrior",
    "name": "Erik the Bold",
    "level": 5,
    "traits": [
      "Courageous",
      "Stubborn"
    ],
    "equipment": {
      "weapon": "Steel Sword",
      "armor": "Chain Mail",
      "accessory": "Warrior's Band"
    }
  }
}
```

### Enemy System Commands

#### Create Enemy Type
```json
{
  "command": "create_enemy_type",
  "params": {
    "type_name": "Vampire Thrall",
    "base_stats": {
      "health": 80,
      "damage": 15,
      "speed": 12
    },
    "resistances": {
      "physical": 0.6,
      "magical": 0.5,
      "mental": 1.0
    },
    "effects": [
      "Blood Drain",
      "Life Steal"
    ],
    "special_abilities": [
      "Bat Form",
      "Blood Frenzy"
    ],
    "behavior": "Aggressive",
    "appearance": "Pale humanoid with fangs and red eyes"
  }
}
```

#### Create Enemy Instance
```json
{
  "command": "create_enemy_instance",
  "params": {
    "type_name": "Vampire Thrall",
    "level": 8,
    "location": {
      "x": 100,
      "y": 200,
      "z": 0
    },
    "modifiers": [
      "Elite",
      "Blood Infused"
    ]
  }
}
```

### Effect System Commands

#### Create Effect Type
```json
{
  "command": "create_effect_type",
  "params": {
    "effect_name": "Vampirism",
    "category": "Physical",
    "duration": -1,
    "stackable": false,
    "properties": {
      "night_vision": true,
      "sunlight_damage": 5,
      "blood_hunger": true,
      "regeneration_in_darkness": 2
    },
    "stages": [
      {
        "name": "Minor Symptoms",
        "duration": 3600,
        "properties": {
          "night_vision": true,
          "sunlight_sensitivity": 0.2
        }
      },
      {
        "name": "Blood Hunger",
        "duration": 7200,
        "properties": {
          "night_vision": true,
          "sunlight_sensitivity": 0.5,
          "blood_hunger": true
        }
      },
      {
        "name": "Full Transformation",
        "duration": -1,
        "properties": {
          "night_vision": true,
          "sunlight_sensitivity": 1.0,
          "blood_hunger": true,
          "bat_form": true,
          "regeneration_in_darkness": 2
        }
      }
    ]
  }
}
```

#### Create Effect Instance
```json
{
  "command": "create_effect_instance",
  "params": {
    "effect_name": "Vampirism",
    "target_id": "character_123",
    "stage": 1,
    "source": "vampire_attack",
    "duration": 3600
  }
}
```

### Dungeon System Commands

#### Create Dungeon Type
```json
{
  "command": "create_dungeon_type",
  "params": {
    "dungeon_name": "Vampire Castle",
    "theme": "Gothic castle with blood-themed architecture",
    "lighting": "Moonlight through stained glass, blood-red torches",
    "environmental_hazards": [
      "Blood pools that heal vampires but damage humans",
      "Sunlight traps that damage vampires",
      "Coffin traps that can imprison players",
      "Bat swarms that obscure vision"
    ],
    "enemy_types": [
      "Vampire Thrall",
      "Blood Mage",
      "Bat Swarm",
      "Vampire Knight"
    ],
    "boss": "The Vampire Lord",
    "special_loot": [
      "Blood vials",
      "Vampiric artifacts",
      "Transformation scrolls"
    ],
    "unique_mechanics": [
      "Vampirism infection",
      "Blood consumption",
      "Sunlight vulnerability",
      "Bat form transformation"
    ]
  }
}
```

#### Create Dungeon Instance
```json
{
  "command": "create_dungeon_instance",
  "params": {
    "dungeon_name": "Vampire Castle",
    "difficulty": "Hard",
    "size": "Large",
    "special_features": [
      "Blood Moon",
      "Ancient Crypt"
    ],
    "loot_multiplier": 1.5
  }
}
```

### Boss System Commands

#### Create Boss Type
```json
{
  "command": "create_boss_type",
  "params": {
    "boss_name": "The Vampire Lord",
    "class": "Vampire/Warrior/Mage hybrid",
    "phases": [
      {
        "name": "Noble",
        "abilities": [
          "Command Thralls",
          "Noble Strike",
          "Blood Shield"
        ],
        "health_percentage": 100
      },
      {
        "name": "Beast",
        "abilities": [
          "Bat Form",
          "Blood Storm",
          "Life Tap"
        ],
        "health_percentage": 66
      },
      {
        "name": "Ancient",
        "abilities": [
          "Blood Curse",
          "Mass Possession",
          "Blood Armor"
        ],
        "health_percentage": 33
      }
    ],
    "weaknesses": [
      "Sunlight",
      "Holy damage",
      "Garlic"
    ],
    "resistances": {
      "physical": 0.8,
      "darkness": 1.0,
      "blood_magic": 1.0
    },
    "drops": [
      "Vampire lord's fang",
      "Blood amulet",
      "Transformation scroll"
    ]
  }
}
```

#### Create Boss Instance
```json
{
  "command": "create_boss_instance",
  "params": {
    "boss_name": "The Vampire Lord",
    "level": 15,
    "location": {
      "x": 500,
      "y": 500,
      "z": 0
    },
    "special_modifiers": [
      "Blood Moon Enhanced",
      "Ancient Bloodline"
    ]
  }
}
```

### Vampire-Specific Commands

#### Create Vampire Character
```json
{
  "command": "create_vampire_character",
  "params": {
    "base_class": "Warrior",
    "name": "Vlad the Nightwalker",
    "vampirism_stage": 3,
    "abilities": [
      "Blood Consumption",
      "Bat Form",
      "Night Vision",
      "Life Steal",
      "Blood Magic"
    ],
    "resistances": {
      "physical": 0.7,
      "magical": 0.6,
      "mental": 0.8,
      "sunlight": -0.5
    },
    "blood_type": "Ancient",
    "age": 300
  }
}
```

#### Create Vampire Enemy
```json
{
  "command": "create_vampire_enemy",
  "params": {
    "type": "Blood Mage",
    "name": "Countess Elizabeth",
    "level": 12,
    "abilities": [
      "Blood Curse",
      "Hemorrhage",
      "Blood Storm",
      "Life Tap"
    ],
    "location": {
      "x": 300,
      "y": 400,
      "z": 0
    },
    "special_modifiers": [
      "Blood Moon Enhanced",
      "Ancient Bloodline"
    ]
  }
}
```

#### Create Blood Effect
```json
{
  "command": "create_blood_effect",
  "params": {
    "effect_name": "Blood Pool",
    "location": {
      "x": 200,
      "y": 300,
      "z": 0
    },
    "size": 5,
    "duration": 300,
    "properties": {
      "heals_vampires": true,
      "damages_humans": true,
      "transmits_vampirism": true,
      "heal_amount": 2,
      "damage_amount": 1
    }
  }
}
```

#### Create Vampire Castle
```json
{
  "command": "create_vampire_castle",
  "params": {
    "name": "Castle Dracula",
    "size": "Large",
    "features": [
      "Blood Moon Altar",
      "Ancient Crypt",
      "Bat Roost",
      "Blood Fountain",
      "Sunlight Traps"
    ],
    "rooms": [
      {
        "type": "Throne Room",
        "boss": "The Vampire Lord",
        "hazards": [
          "Blood Pools",
          "Bat Swarms"
        ]
      },
      {
        "type": "Dining Hall",
        "enemies": [
          "Vampire Thrall",
          "Blood Mage"
        ],
        "hazards": [
          "Blood Pools"
        ]
      },
      {
        "type": "Crypt",
        "enemies": [
          "Vampire Knight",
          "Bat Swarms"
        ],
        "hazards": [
          "Coffin Traps"
        ]
      }
    ],
    "loot_tables": [
      "Blood Vials",
      "Vampiric Artifacts",
      "Transformation Scrolls"
    ]
  }
}
```

#### Create Vampire Lord
```json
{
  "command": "create_vampire_lord",
  "params": {
    "name": "Count Dracula",
    "level": 20,
    "phases": [
      {
        "name": "Noble",
        "abilities": [
          "Command Thralls",
          "Noble Strike",
          "Blood Shield"
        ],
        "appearance": "Aristocratic vampire with fine clothing"
      },
      {
        "name": "Beast",
        "abilities": [
          "Bat Form",
          "Blood Storm",
          "Life Tap"
        ],
        "appearance": "Bat-like creature with elongated limbs"
      },
      {
        "name": "Ancient",
        "abilities": [
          "Blood Curse",
          "Mass Possession",
          "Blood Armor"
        ],
        "appearance": "Ancient vampire with blood-red aura"
      }
    ],
    "weaknesses": [
      "Sunlight",
      "Holy damage",
      "Garlic"
    ],
    "resistances": {
      "physical": 0.8,
      "darkness": 1.0,
      "blood_magic": 1.0
    },
    "drops": [
      "Vampire lord's fang",
      "Blood amulet",
      "Transformation scroll"
    ],
    "location": {
      "x": 500,
      "y": 500,
      "z": 0
    }
  }
}
```

## Level and Actor Commands

### Create Level
```json
{
  "command": "CreateLevel",
  "params": {
    "levelName": "TestLevel",
    "template": "EmptyLevel",
    "savePath": "/Game/Maps/TestLevel"
  }
}
```

### Add Actor
```json
{
  "command": "AddActor",
  "params": {
    "actorClass": "StaticMeshActor",
    "actorName": "Floor",
    "location": {"x": 0, "y": 0, "z": 0},
    "rotation": {"pitch": 0, "yaw": 0, "roll": 0},
    "scale": {"x": 10, "y": 10, "z": 1},
    "staticMesh": "/Engine/BasicShapes/Plane.Plane"
  }
}
```

### Save Level
```json
{
  "command": "SaveLevel",
  "params": {
    "levelName": "TestLevel",
    "savePath": "/Game/Maps/TestLevel"
  }
}
```

### Refresh Content Browser
```json
{
  "command": "RefreshContentBrowser",
  "params": {}
}
```

## Blueprint Node Commands

### Add Blueprint Node
```json
{
  "command": "AddBlueprintNode",
  "params": {
    "blueprintName": "BP_FCCharacter",
    "nodeType": "InputAxis",
    "nodeName": "MoveForward",
    "location": [0, 0],
    "connections": {
      "AxisValue": {
        "targetNode": "AddMovementInput",
        "targetPin": "ScaleValue"
      }
    }
  }
}
```

### Add Input Mapping
```json
{
  "command": "AddInputMapping",
  "params": {
    "name": "MoveForward",
    "type": "Axis",
    "scale": 1.0,
    "keys": ["W", "S"]
  }
}
```

## Modified ExecuteCommand Function

```cpp
FString UUnrealMCPBridge::ExecuteCommand(const FString& CommandType, const TSharedPtr<FJsonObject>& Params)
{
    UE_LOG(LogTemp, Display, TEXT("UnrealMCPBridge: Executing command: %s"), *CommandType);
    
    TPromise<FString> Promise;
    TFuture<FString> Future = Promise.GetFuture();
    
    AsyncTask(ENamedThreads::GameThread, [this, CommandType, Params, Promise = MoveTemp(Promise)]() mutable
    {
        TSharedPtr<FJsonObject> ResponseJson = MakeShareable(new FJsonObject);
        
        try
        {
            TSharedPtr<FJsonObject> ResultJson;
            
            if (CommandType == TEXT("ping"))
            {
                ResultJson = MakeShareable(new FJsonObject);
                ResultJson->SetStringField(TEXT("message"), TEXT("pong"));
            }
            // Actor Commands
            else if (CommandType == TEXT("get_actors_in_level") || 
                     CommandType == TEXT("find_actors_by_name") ||
                     CommandType == TEXT("create_actor") || 
                     CommandType == TEXT("delete_actor") || 
                     CommandType == TEXT("set_actor_transform") ||
                     CommandType == TEXT("get_actor_properties") ||
                     CommandType == TEXT("AddActor"))
            {
                ResultJson = ActorCommands->HandleCommand(CommandType, Params);
            }
            // Editor Commands
            else if (CommandType == TEXT("focus_viewport") || 
                     CommandType == TEXT("take_screenshot") ||
                     CommandType == TEXT("CreateLevel") ||
                     CommandType == TEXT("SaveLevel") ||
                     CommandType == TEXT("RefreshContentBrowser"))
            {
                ResultJson = EditorCommands->HandleCommand(CommandType, Params);
            }
            // Blueprint Commands
            else if (CommandType == TEXT("create_blueprint") || 
                     CommandType == TEXT("add_component_to_blueprint") || 
                     CommandType == TEXT("set_component_property") || 
                     CommandType == TEXT("set_physics_properties") || 
                     CommandType == TEXT("compile_blueprint") || 
                     CommandType == TEXT("spawn_blueprint_actor") || 
                     CommandType == TEXT("set_blueprint_property") || 
                     CommandType == TEXT("set_static_mesh_properties"))
            {
                ResultJson = BlueprintCommands->HandleCommand(CommandType, Params);
            }
            // Blueprint Node Commands
            else if (CommandType == TEXT("connect_blueprint_nodes") || 
                     CommandType == TEXT("create_input_mapping") || 
                     CommandType == TEXT("add_blueprint_get_self_component_reference") ||
                     CommandType == TEXT("add_blueprint_self_reference") ||
                     CommandType == TEXT("find_blueprint_nodes") ||
                     CommandType == TEXT("add_blueprint_event_node") ||
                     CommandType == TEXT("add_blueprint_input_action_node") ||
                     CommandType == TEXT("add_blueprint_function_node") ||
                     CommandType == TEXT("add_blueprint_get_component_node") ||
                     CommandType == TEXT("add_blueprint_variable") ||
                     CommandType == TEXT("AddBlueprintNode") ||
                     CommandType == TEXT("AddInputMapping"))
            {
                ResultJson = BlueprintNodeCommands->HandleCommand(CommandType, Params);
            }
            // Game Commands
            else if (CommandType == TEXT("create_character_class") ||
                     CommandType == TEXT("create_character_instance") ||
                     CommandType == TEXT("create_enemy_type") ||
                     CommandType == TEXT("create_enemy_instance") ||
                     CommandType == TEXT("create_effect_type") ||
                     CommandType == TEXT("create_effect_instance") ||
                     CommandType == TEXT("create_dungeon_type") ||
                     CommandType == TEXT("create_dungeon_instance") ||
                     CommandType == TEXT("create_boss_type") ||
                     CommandType == TEXT("create_boss_instance") ||
                     CommandType == TEXT("create_vampire_character") ||
                     CommandType == TEXT("create_vampire_enemy") ||
                     CommandType == TEXT("create_blood_effect") ||
                     CommandType == TEXT("create_vampire_castle") ||
                     CommandType == TEXT("create_vampire_lord"))
            {
                ResultJson = GameCommands->HandleCommand(CommandType, Params);
            }
            else
            {
                ResponseJson->SetStringField(TEXT("status"), TEXT("error"));
                ResponseJson->SetStringField(TEXT("error"), FString::Printf(TEXT("Unknown command: %s"), *CommandType));
                
                FString ResultString;
                TSharedRef<TJsonWriter<>> Writer = TJsonWriterFactory<>::Create(&ResultString);
                FJsonSerializer::Serialize(ResponseJson.ToSharedRef(), Writer);
                Promise.SetValue(ResultString);
                return;
            }
            
            ResponseJson->SetStringField(TEXT("status"), TEXT("success"));
            ResponseJson->SetObjectField(TEXT("result"), ResultJson);
        }
        catch (const std::exception& e)
        {
            ResponseJson->SetStringField(TEXT("status"), TEXT("error"));
            ResponseJson->SetStringField(TEXT("error"), UTF8_TO_TCHAR(e.what()));
        }
        
        FString ResultString;
        TSharedRef<TJsonWriter<>> Writer = TJsonWriterFactory<>::Create(&ResultString);
        FJsonSerializer::Serialize(ResponseJson.ToSharedRef(), Writer);
        Promise.SetValue(ResultString);
    });
    
    return Future.Get();
}
```

## Implementation Tips

1. **Work in parallel**: Have one person create file structure and headers while another prepares code blocks

2. **Copy-paste intelligently**: Use search and replace to quickly change references from class methods to utility methods

3. **Build incrementally**: Build after each major step to catch errors quickly

4. **Comment out rather than delete**: If unsure, comment out code temporarily

5. **Focus on correctness over elegance**: Get it working first

6. **Use IDE features**: Use IDE refactoring tools to help with moving code

## Process Summary
1. Create file structure
2. Copy utility methods to CommonUtils
3. Copy command handlers to respective files
4. Update references to use the new structure
5. Modify UnrealMCPBridge.cpp to delegate
6. Final build and test 