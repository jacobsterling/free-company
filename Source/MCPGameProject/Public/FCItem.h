// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "FCItem.generated.h"

UENUM(BlueprintType)
enum class EItemType : uint8
{
	Weapon UMETA(DisplayName = "Weapon"),
	Consumable UMETA(DisplayName = "Consumable"),
	Material UMETA(DisplayName = "Material"),
	Quest UMETA(DisplayName = "Quest"),
	Torch UMETA(DisplayName = "Torch")
};

UCLASS()
class MCPGAMEPROJECT_API AFCItem : public AActor
{
	GENERATED_BODY()

public:
	// Sets default values for this actor's properties
	AFCItem();

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

public:
	// Called every frame
	virtual void Tick(float DeltaTime) override;

	// Item name getter and setter
	UFUNCTION(BlueprintCallable, Category = "Item")
	FString GetItemName() const { return ItemName; }

	UFUNCTION(BlueprintCallable, Category = "Item")
	void SetItemName(const FString& NewItemName);

	// Item description getter and setter
	UFUNCTION(BlueprintCallable, Category = "Item")
	FString GetItemDescription() const { return ItemDescription; }

	UFUNCTION(BlueprintCallable, Category = "Item")
	void SetItemDescription(const FString& NewItemDescription);

	// Item type getter and setter
	UFUNCTION(BlueprintCallable, Category = "Item")
	EItemType GetItemType() const { return ItemType; }

	UFUNCTION(BlueprintCallable, Category = "Item")
	void SetItemType(EItemType NewItemType);

	// Item value getter and setter
	UFUNCTION(BlueprintCallable, Category = "Item")
	int32 GetItemValue() const { return ItemValue; }

	UFUNCTION(BlueprintCallable, Category = "Item")
	void SetItemValue(int32 NewItemValue);

	// Item weight getter and setter
	UFUNCTION(BlueprintCallable, Category = "Item")
	float GetItemWeight() const { return ItemWeight; }

	UFUNCTION(BlueprintCallable, Category = "Item")
	void SetItemWeight(float NewItemWeight);

	// Item mesh getter and setter
	UFUNCTION(BlueprintCallable, Category = "Item")
	UStaticMeshComponent* GetItemMesh() const { return ItemMesh; }

	// Use item function
	UFUNCTION(BlueprintCallable, Category = "Item")
	virtual void Use(class AFCCharacter* Character);

protected:
	// Item properties
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Item")
	FString ItemName;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Item")
	FString ItemDescription;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Item")
	EItemType ItemType;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Item")
	int32 ItemValue;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Item")
	float ItemWeight;

	// Item mesh
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Item")
	class UStaticMeshComponent* ItemMesh;
}; 