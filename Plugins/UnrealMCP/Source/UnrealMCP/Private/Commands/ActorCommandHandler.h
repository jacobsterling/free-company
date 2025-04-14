#pragma once

#include "CoreMinimal.h"
#include "Json.h"

/**
 * Handler for Actor commands in the MCP system
 */
class UNREALMCP_API FActorCommandHandler
{
public:
    FActorCommandHandler();
    
    /**
     * Handles the AddActor command which creates an actor in the level
     * 
     * @param Params JSON parameters including actor_class, location, rotation, scale, name
     * @return JSON response with success status and actor details
     */
    TSharedPtr<FJsonObject> HandleAddActor(const TSharedPtr<FJsonObject>& Params);
}; 