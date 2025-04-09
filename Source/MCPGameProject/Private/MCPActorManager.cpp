#include "MCPActorManager.h"
#include "MCPGameProject.h"
#include "Engine/World.h"
#include "Engine/StaticMeshActor.h"
#include "Engine/DirectionalLight.h"
#include "Engine/SkyLight.h"
#include "GameFramework/Actor.h"
#include "Json/Public/JsonObject.h"
#include "Json/Public/JsonSerializer.h"
#include "Editor.h"
#include "EditorLevelUtils.h"
#include "FileHelpers.h"
#include "AssetRegistry/AssetRegistryModule.h"

UMCPActorManager::UMCPActorManager()
{
    // Register commands
    RegisterCommand("AddActor", &UMCPActorManager::AddActor);
    RegisterCommand("CreateLevel", &UMCPActorManager::CreateLevel);
    RegisterCommand("SetComponentProperty", &UMCPActorManager::SetComponentProperty);
}

void UMCPActorManager::RegisterCommand(const FString& CommandName, CommandFunction Function)
{
    CommandHandlers.Add(CommandName, Function);
}

bool UMCPActorManager::HandleCommand(const FString& CommandName, const TSharedPtr<FJsonObject>& Params, TSharedPtr<FJsonObject>& OutResponse)
{
    if (CommandFunction* Function = CommandHandlers.Find(CommandName))
    {
        return (this->*(*Function))(Params, OutResponse);
    }
    
    OutResponse->SetStringField("error", FString::Printf(TEXT("Unknown command: %s"), *CommandName));
    return false;
}

bool UMCPActorManager::CreateLevel(const TSharedPtr<FJsonObject>& Params, TSharedPtr<FJsonObject>& OutResponse)
{
    // Get required parameters
    FString LevelName;
    FString Template;
    if (!Params->TryGetStringField("levelName", LevelName) || !Params->TryGetStringField("template", Template))
    {
        OutResponse->SetStringField("error", "Missing required parameters: levelName and template");
        return false;
    }

    // Create a new level
    UWorld* NewWorld = EditorLevelUtils::CreateNewLevel(LevelName, Template);
    if (!NewWorld)
    {
        OutResponse->SetStringField("error", "Failed to create level");
        return false;
    }

    // Save the level
    FString PackagePath = FString::Printf(TEXT("/Game/Maps/%s"), *LevelName);
    FString FullPath = FString::Printf(TEXT("%s.%s"), *PackagePath, *LevelName);
    
    if (!EditorLevelUtils::SaveLevel(NewWorld, *FullPath))
    {
        OutResponse->SetStringField("error", "Failed to save level");
        return false;
    }

    // Set success response
    OutResponse->SetStringField("status", "success");
    OutResponse->SetStringField("levelName", LevelName);
    return true;
}

bool UMCPActorManager::AddActor(const TSharedPtr<FJsonObject>& Params, TSharedPtr<FJsonObject>& OutResponse)
{
    // Get required parameters
    FString ActorClass;
    FString ActorName;
    if (!Params->TryGetStringField("actorClass", ActorClass) || !Params->TryGetStringField("actorName", ActorName))
    {
        OutResponse->SetStringField("error", "Missing required parameters: actorClass and actorName");
        return false;
    }

    // Get optional parameters
    FVector Location = FVector::ZeroVector;
    FRotator Rotation = FRotator::ZeroRotator;
    FVector Scale = FVector(1.0f);

    if (const TSharedPtr<FJsonObject>* LocationObj = nullptr; Params->TryGetObjectField("location", LocationObj))
    {
        Location = FVector(
            (*LocationObj)->GetNumberField("x"),
            (*LocationObj)->GetNumberField("y"),
            (*LocationObj)->GetNumberField("z")
        );
    }

    if (const TSharedPtr<FJsonObject>* RotationObj = nullptr; Params->TryGetObjectField("rotation", RotationObj))
    {
        Rotation = FRotator(
            (*RotationObj)->GetNumberField("pitch"),
            (*RotationObj)->GetNumberField("yaw"),
            (*RotationObj)->GetNumberField("roll")
        );
    }

    if (const TSharedPtr<FJsonObject>* ScaleObj = nullptr; Params->TryGetObjectField("scale", ScaleObj))
    {
        Scale = FVector(
            (*ScaleObj)->GetNumberField("x"),
            (*ScaleObj)->GetNumberField("y"),
            (*ScaleObj)->GetNumberField("z")
        );
    }

    // Get the current editor world
    UWorld* World = GEditor->GetEditorWorldContext().World();
    if (!World)
    {
        OutResponse->SetStringField("error", "No valid world found");
        return false;
    }

    FActorSpawnParameters SpawnParams;
    SpawnParams.Name = *ActorName;

    AActor* NewActor = nullptr;
    
    // Handle different actor types
    if (ActorClass == "StaticMeshActor")
    {
        FString StaticMeshPath;
        if (Params->TryGetStringField("staticMesh", StaticMeshPath))
        {
            UStaticMesh* StaticMesh = Cast<UStaticMesh>(StaticMeshPath.TryLoad());
            if (StaticMesh)
            {
                AStaticMeshActor* MeshActor = World->SpawnActor<AStaticMeshActor>(AStaticMeshActor::StaticClass(), Location, Rotation, SpawnParams);
                if (MeshActor)
                {
                    MeshActor->GetStaticMeshComponent()->SetStaticMesh(StaticMesh);
                    MeshActor->SetActorScale3D(Scale);
                    NewActor = MeshActor;
                }
            }
        }
        else
        {
            NewActor = World->SpawnActor<AStaticMeshActor>(AStaticMeshActor::StaticClass(), Location, Rotation, SpawnParams);
        }
    }
    else if (ActorClass == "DirectionalLight")
    {
        NewActor = World->SpawnActor<ADirectionalLight>(ADirectionalLight::StaticClass(), Location, Rotation, SpawnParams);
    }
    else if (ActorClass == "SkyLight")
    {
        NewActor = World->SpawnActor<ASkyLight>(ASkyLight::StaticClass(), Location, Rotation, SpawnParams);
    }
    else
    {
        // Try to find the class by name
        UClass* ActorClassObj = FindObject<UClass>(nullptr, *ActorClass);
        if (ActorClassObj)
        {
            NewActor = World->SpawnActor<AActor>(ActorClassObj, Location, Rotation, SpawnParams);
        }
        else
        {
            OutResponse->SetStringField("error", FString::Printf(TEXT("Unknown actor class: %s"), *ActorClass));
            return false;
        }
    }

    if (!NewActor)
    {
        OutResponse->SetStringField("error", "Failed to spawn actor");
        return false;
    }

    // Set scale
    NewActor->SetActorScale3D(Scale);

    // Broadcast delegate
    OnActorAdded.Broadcast(NewActor);

    // Set success response
    OutResponse->SetStringField("status", "success");
    OutResponse->SetStringField("actorName", ActorName);
    return true;
}

bool UMCPActorManager::SetComponentProperty(const TSharedPtr<FJsonObject>& Params, TSharedPtr<FJsonObject>& OutResponse)
{
    // Get required parameters
    FString BlueprintName;
    FString ComponentName;
    FString PropertyName;
    if (!Params->TryGetStringField("blueprintName", BlueprintName) || 
        !Params->TryGetStringField("componentName", ComponentName) || 
        !Params->TryGetStringField("propertyName", PropertyName))
    {
        OutResponse->SetStringField("error", "Missing required parameters: blueprintName, componentName, and propertyName");
        return false;
    }

    // Get the property value
    TSharedPtr<FJsonValue> PropertyValue;
    if (!Params->TryGetField("propertyValue", PropertyValue))
    {
        OutResponse->SetStringField("error", "Missing required parameter: propertyValue");
        return false;
    }

    // Find the blueprint
    FString BlueprintPath = FString::Printf(TEXT("/Game/Blueprints/%s.%s_C"), *BlueprintName, *BlueprintName);
    UBlueprint* Blueprint = Cast<UBlueprint>(StaticLoadObject(UBlueprint::StaticClass(), nullptr, *BlueprintPath));
    if (!Blueprint)
    {
        OutResponse->SetStringField("error", FString::Printf(TEXT("Blueprint not found: %s"), *BlueprintPath));
        return false;
    }

    // Find the component
    USCS_Node* ComponentNode = nullptr;
    for (USCS_Node* Node : Blueprint->SimpleConstructionScript->GetAllNodes())
    {
        if (Node->GetVariableName().ToString() == ComponentName)
        {
            ComponentNode = Node;
            break;
        }
    }

    if (!ComponentNode)
    {
        OutResponse->SetStringField("error", FString::Printf(TEXT("Component not found: %s"), *ComponentName));
        return false;
    }

    // Set the property value based on its type
    UObject* ComponentTemplate = ComponentNode->ComponentTemplate;
    if (!ComponentTemplate)
    {
        OutResponse->SetStringField("error", "Component template not found");
        return false;
    }

    // Handle different property types
    if (PropertyValue->IsString())
    {
        FString StringValue = PropertyValue->AsString();
        if (PropertyName == "SkeletalMesh" || PropertyName == "AnimClass")
        {
            UObject* Asset = StaticLoadObject(UObject::StaticClass(), nullptr, *StringValue);
            if (Asset)
            {
                ComponentTemplate->SetPropertyValueByName(*PropertyName, Asset);
            }
            else
            {
                OutResponse->SetStringField("error", FString::Printf(TEXT("Asset not found: %s"), *StringValue));
                return false;
            }
        }
        else
        {
            ComponentTemplate->SetPropertyValueByName(*PropertyName, *StringValue);
        }
    }
    else if (PropertyValue->IsBool())
    {
        bool BoolValue = PropertyValue->AsBool();
        ComponentTemplate->SetPropertyValueByName(*PropertyName, BoolValue);
    }
    else if (PropertyValue->IsNumber())
    {
        double NumberValue = PropertyValue->AsNumber();
        ComponentTemplate->SetPropertyValueByName(*PropertyName, NumberValue);
    }
    else
    {
        OutResponse->SetStringField("error", "Unsupported property value type");
        return false;
    }

    // Compile the blueprint
    FKismetCompilerContext CompilerContext(Blueprint, FCompilerResultsLog(), FBlueprintCompileOptions());
    CompilerContext.Compile();

    // Set success response
    OutResponse->SetStringField("status", "success");
    return true;
} 