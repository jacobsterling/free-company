#pragma once

#include "CoreMinimal.h"
#include "Dom/JsonObject.h"
#include "Dom/JsonValue.h"
#include "Serialization/JsonWriter.h"
#include "Serialization/JsonSerializer.h"

/**
 * Common utility functions for the UnrealMCP system to handle JSON operations and common tasks
 */
class UNREALMCP_API FUnrealMCPCommonUtils
{
public:
    /**
     * Creates a standard error response JSON object
     * @param ErrorMessage - The error message to include
     * @return A JSON object with success=false and the error message
     */
    static TSharedPtr<FJsonObject> CreateErrorResponse(const FString& ErrorMessage)
    {
        TSharedPtr<FJsonObject> ResponseObj = MakeShared<FJsonObject>();
        ResponseObj->SetBoolField("success", false);
        ResponseObj->SetStringField("error", ErrorMessage);
        return ResponseObj;
    }

    /**
     * Creates a standard success response JSON object
     * @param Message - Optional message to include
     * @return A JSON object with success=true and optional message
     */
    static TSharedPtr<FJsonObject> CreateSuccessResponse(const FString& Message = TEXT(""))
    {
        TSharedPtr<FJsonObject> ResponseObj = MakeShared<FJsonObject>();
        ResponseObj->SetBoolField("success", true);
        if (!Message.IsEmpty())
        {
            ResponseObj->SetStringField("message", Message);
        }
        return ResponseObj;
    }

    /**
     * Extracts a FVector from a JSON object
     * @param JsonObject - The JSON object containing the vector data
     * @param FieldName - The name of the field containing the vector data
     * @param DefaultValue - Default vector to use if the field is missing or invalid
     * @return The extracted FVector or the default value
     */
    static FVector GetVectorFromJson(const TSharedPtr<FJsonObject>& JsonObject, const FString& FieldName, const FVector& DefaultValue = FVector::ZeroVector)
    {
        if (!JsonObject->HasField(FieldName))
        {
            return DefaultValue;
        }

        const TSharedPtr<FJsonObject>* VectorObj;
        if (!JsonObject->TryGetObjectField(FieldName, VectorObj))
        {
            return DefaultValue;
        }

        float X = DefaultValue.X;
        float Y = DefaultValue.Y;
        float Z = DefaultValue.Z;

        if ((*VectorObj)->HasTypedField<EJson::Number>("x"))
        {
            X = (*VectorObj)->GetNumberField("x");
        }
        if ((*VectorObj)->HasTypedField<EJson::Number>("y"))
        {
            Y = (*VectorObj)->GetNumberField("y");
        }
        if ((*VectorObj)->HasTypedField<EJson::Number>("z"))
        {
            Z = (*VectorObj)->GetNumberField("z");
        }

        return FVector(X, Y, Z);
    }

    /**
     * Extracts a FRotator from a JSON object
     * @param JsonObject - The JSON object containing the rotator data
     * @param FieldName - The name of the field containing the rotator data
     * @param DefaultValue - Default rotator to use if the field is missing or invalid
     * @return The extracted FRotator or the default value
     */
    static FRotator GetRotatorFromJson(const TSharedPtr<FJsonObject>& JsonObject, const FString& FieldName, const FRotator& DefaultValue = FRotator::ZeroRotator)
    {
        if (!JsonObject->HasField(FieldName))
        {
            return DefaultValue;
        }

        const TSharedPtr<FJsonObject>* RotatorObj;
        if (!JsonObject->TryGetObjectField(FieldName, RotatorObj))
        {
            return DefaultValue;
        }

        float Pitch = DefaultValue.Pitch;
        float Yaw = DefaultValue.Yaw;
        float Roll = DefaultValue.Roll;

        // Support both pitch/yaw/roll and p/y/r formats
        if ((*RotatorObj)->HasTypedField<EJson::Number>("pitch"))
        {
            Pitch = (*RotatorObj)->GetNumberField("pitch");
        }
        else if ((*RotatorObj)->HasTypedField<EJson::Number>("p"))
        {
            Pitch = (*RotatorObj)->GetNumberField("p");
        }

        if ((*RotatorObj)->HasTypedField<EJson::Number>("yaw"))
        {
            Yaw = (*RotatorObj)->GetNumberField("yaw");
        }
        else if ((*RotatorObj)->HasTypedField<EJson::Number>("y"))
        {
            Yaw = (*RotatorObj)->GetNumberField("y");
        }

        if ((*RotatorObj)->HasTypedField<EJson::Number>("roll"))
        {
            Roll = (*RotatorObj)->GetNumberField("roll");
        }
        else if ((*RotatorObj)->HasTypedField<EJson::Number>("r"))
        {
            Roll = (*RotatorObj)->GetNumberField("r");
        }

        return FRotator(Pitch, Yaw, Roll);
    }

    /**
     * Converts a JSON object to a string
     * @param JsonObject - The JSON object to convert
     * @param bPrettyPrint - Whether to format the JSON with whitespace (default: false)
     * @return String representation of the JSON object
     */
    static FString JsonObjectToString(const TSharedPtr<FJsonObject>& JsonObject, bool bPrettyPrint = false)
    {
        FString OutputString;
        TSharedRef<TJsonWriter<>> Writer = bPrettyPrint ?
            TJsonWriterFactory<>::Create(&OutputString, 0) :
            TJsonWriterFactory<>::Create(&OutputString);
        FJsonSerializer::Serialize(JsonObject.ToSharedRef(), Writer);
        return OutputString;
    }
}; 