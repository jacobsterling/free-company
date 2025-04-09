#pragma once

#include "CoreMinimal.h"
#include "UObject/NoExportTypes.h"
#include "Json/Public/JsonObject.h"
#include "MCPActorManager.generated.h"

DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnActorAdded, AActor*, NewActor);

UCLASS()
class MCPGAMEPROJECT_API UMCPActorManager : public UObject
{
    GENERATED_BODY()

public:
    UMCPActorManager();

    // Command handling
    typedef bool (UMCPActorManager::*CommandFunction)(const TSharedPtr<FJsonObject>&, TSharedPtr<FJsonObject>&);
    void RegisterCommand(const FString& CommandName, CommandFunction Function);
    bool HandleCommand(const FString& CommandName, const TSharedPtr<FJsonObject>& Params, TSharedPtr<FJsonObject>& OutResponse);

    // Actor management
    bool AddActor(const TSharedPtr<FJsonObject>& Params, TSharedPtr<FJsonObject>& OutResponse);
    
    // Level management
    bool CreateLevel(const TSharedPtr<FJsonObject>& Params, TSharedPtr<FJsonObject>& OutResponse);
    
    // Blueprint management
    bool SetComponentProperty(const TSharedPtr<FJsonObject>& Params, TSharedPtr<FJsonObject>& OutResponse);

    // Delegates
    UPROPERTY(BlueprintAssignable, Category = "MCP|Actor")
    FOnActorAdded OnActorAdded;

private:
    TMap<FString, CommandFunction> CommandHandlers;
}; 