#include "ActorCommandHandler.h"
#include "Commands/UnrealMCPCommonUtils.h"
#include "Engine/World.h"
#include "Editor.h"
#include "Engine/StaticMeshActor.h"
#include "Engine/DirectionalLight.h"
#include "Engine/PointLight.h"
#include "Engine/SpotLight.h"
#include "Camera/CameraActor.h"
#include "GameFramework/Character.h"
#include "Components/StaticMeshComponent.h"
#include "EditorSubsystem.h"
#include "Subsystems/EditorActorSubsystem.h"
#include "Kismet/GameplayStatics.h"

// Use our MCP log category
DEFINE_LOG_CATEGORY_STATIC(LogMCP, Log, All);

FActorCommandHandler::FActorCommandHandler()
{
}

TSharedPtr<FJsonObject> FActorCommandHandler::HandleAddActor(const TSharedPtr<FJsonObject>& Params)
{
    // Create response object
    TSharedPtr<FJsonObject> ResultObj = MakeShared<FJsonObject>();

    // Get required parameters
    FString ActorClass;
    if (!Params->TryGetStringField("actor_class", ActorClass))
    {
        UE_LOG(LogMCP, Warning, TEXT("ActorCommandHandler: Missing actor_class parameter"));
        return FUnrealMCPCommonUtils::CreateErrorResponse("Missing actor_class parameter");
    }

    // Get optional parameters
    FVector Location(0.0f, 0.0f, 0.0f);
    FRotator Rotation(0.0f, 0.0f, 0.0f);
    FVector Scale(1.0f, 1.0f, 1.0f);

    if (Params->HasField("location"))
    {
        Location = FUnrealMCPCommonUtils::GetVectorFromJson(Params, "location");
        UE_LOG(LogMCP, Log, TEXT("ActorCommandHandler: Using location from params: X=%f, Y=%f, Z=%f"), 
               Location.X, Location.Y, Location.Z);
    }
    
    if (Params->HasField("rotation"))
    {
        Rotation = FUnrealMCPCommonUtils::GetRotatorFromJson(Params, "rotation");
        UE_LOG(LogMCP, Log, TEXT("ActorCommandHandler: Using rotation from params: P=%f, Y=%f, R=%f"), 
               Rotation.Pitch, Rotation.Yaw, Rotation.Roll);
    }
    
    if (Params->HasField("scale"))
    {
        Scale = FUnrealMCPCommonUtils::GetVectorFromJson(Params, "scale");
        UE_LOG(LogMCP, Log, TEXT("ActorCommandHandler: Using scale from params: X=%f, Y=%f, Z=%f"), 
               Scale.X, Scale.Y, Scale.Z);
    }

    FString ActorName;
    if (Params->TryGetStringField("name", ActorName))
    {
        UE_LOG(LogMCP, Log, TEXT("ActorCommandHandler: Using name from params: %s"), *ActorName);
    }
    else
    {
        ActorName = FString::Printf(TEXT("Actor_%s_%d"), *ActorClass, FMath::RandRange(1000, 9999));
        UE_LOG(LogMCP, Log, TEXT("ActorCommandHandler: Generated name: %s"), *ActorName);
    }

    // Get world context
    UWorld* World = GEditor ? GEditor->GetEditorWorldContext().World() : nullptr;
    if (!World)
    {
        UE_LOG(LogMCP, Error, TEXT("ActorCommandHandler: Failed to get editor world"));
        return FUnrealMCPCommonUtils::CreateErrorResponse("Failed to get editor world");
    }

    // Spawn parameters
    FActorSpawnParameters SpawnParams;
    SpawnParams.Name = *ActorName;
    
    // Create the actor based on type
    AActor* NewActor = nullptr;
    
    UE_LOG(LogMCP, Log, TEXT("ActorCommandHandler: Attempting to spawn actor of class: %s"), *ActorClass);
    
    if (ActorClass.Equals("Character", ESearchCase::IgnoreCase))
    {
        NewActor = World->SpawnActor<ACharacter>(ACharacter::StaticClass(), Location, Rotation, SpawnParams);
        UE_LOG(LogMCP, Log, TEXT("ActorCommandHandler: Spawning Character"));
    }
    else if (ActorClass.Equals("StaticMeshActor", ESearchCase::IgnoreCase))
    {
        NewActor = World->SpawnActor<AStaticMeshActor>(AStaticMeshActor::StaticClass(), Location, Rotation, SpawnParams);
        UE_LOG(LogMCP, Log, TEXT("ActorCommandHandler: Spawning StaticMeshActor"));
    }
    else if (ActorClass.Equals("PointLight", ESearchCase::IgnoreCase))
    {
        NewActor = World->SpawnActor<APointLight>(APointLight::StaticClass(), Location, Rotation, SpawnParams);
        UE_LOG(LogMCP, Log, TEXT("ActorCommandHandler: Spawning PointLight"));
    }
    else if (ActorClass.Equals("SpotLight", ESearchCase::IgnoreCase))
    {
        NewActor = World->SpawnActor<ASpotLight>(ASpotLight::StaticClass(), Location, Rotation, SpawnParams);
        UE_LOG(LogMCP, Log, TEXT("ActorCommandHandler: Spawning SpotLight"));
    }
    else if (ActorClass.Equals("DirectionalLight", ESearchCase::IgnoreCase))
    {
        NewActor = World->SpawnActor<ADirectionalLight>(ADirectionalLight::StaticClass(), Location, Rotation, SpawnParams);
        UE_LOG(LogMCP, Log, TEXT("ActorCommandHandler: Spawning DirectionalLight"));
    }
    else if (ActorClass.Equals("CameraActor", ESearchCase::IgnoreCase))
    {
        NewActor = World->SpawnActor<ACameraActor>(ACameraActor::StaticClass(), Location, Rotation, SpawnParams);
        UE_LOG(LogMCP, Log, TEXT("ActorCommandHandler: Spawning CameraActor"));
    }
    else
    {
        // Try to find the class dynamically
        UClass* ClassObj = FindObject<UClass>(ANY_PACKAGE, *ActorClass);
        if (ClassObj)
        {
            NewActor = World->SpawnActor(ClassObj, &Location, &Rotation, SpawnParams);
            UE_LOG(LogMCP, Log, TEXT("ActorCommandHandler: Spawning dynamic class: %s"), *ActorClass);
        }
        else
        {
            UE_LOG(LogMCP, Error, TEXT("ActorCommandHandler: Unknown actor class: %s"), *ActorClass);
            return FUnrealMCPCommonUtils::CreateErrorResponse(FString::Printf(TEXT("Unknown actor class: %s"), *ActorClass));
        }
    }

    if (NewActor)
    {
        // Set scale
        NewActor->SetActorScale3D(Scale);
        
        // Set actor label (name in editor)
        NewActor->SetActorLabel(ActorName);
        
        UE_LOG(LogMCP, Log, TEXT("ActorCommandHandler: Successfully spawned actor: %s"), *ActorName);
        
        // Create success response with actor details
        ResultObj->SetBoolField("success", true);
        ResultObj->SetStringField("actor_name", ActorName);
        ResultObj->SetStringField("actor_class", ActorClass);
        
        TSharedPtr<FJsonObject> LocationObj = MakeShared<FJsonObject>();
        LocationObj->SetNumberField("x", Location.X);
        LocationObj->SetNumberField("y", Location.Y);
        LocationObj->SetNumberField("z", Location.Z);
        ResultObj->SetObjectField("location", LocationObj);
        
        return ResultObj;
    }
    else
    {
        UE_LOG(LogMCP, Error, TEXT("ActorCommandHandler: Failed to spawn actor"));
        return FUnrealMCPCommonUtils::CreateErrorResponse("Failed to spawn actor");
    }
} 