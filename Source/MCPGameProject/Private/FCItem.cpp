// Fill out your copyright notice in the Description page of Project Settings.

#include "FCItem.h"
#include "Components/StaticMeshComponent.h"
#include "FCCharacter.h"

// Sets default values
AFCItem::AFCItem()
{
	// Set this actor to call Tick() every frame
	PrimaryActorTick.bCanEverTick = true;

	// Create item mesh component
	ItemMesh = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("ItemMesh"));
	RootComponent = ItemMesh;

	// Set default values for item properties
	ItemName = TEXT("Item");
	ItemDescription = TEXT("A generic item.");
	ItemType = EItemType::Material;
	ItemValue = 0;
	ItemWeight = 1.0f;
}

// Called when the game starts or when spawned
void AFCItem::BeginPlay()
{
	Super::BeginPlay();
}

// Called every frame
void AFCItem::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);
}

// Item name setter
void AFCItem::SetItemName(const FString& NewItemName)
{
	ItemName = NewItemName;
}

// Item description setter
void AFCItem::SetItemDescription(const FString& NewItemDescription)
{
	ItemDescription = NewItemDescription;
}

// Item type setter
void AFCItem::SetItemType(EItemType NewItemType)
{
	ItemType = NewItemType;
}

// Item value setter
void AFCItem::SetItemValue(int32 NewItemValue)
{
	ItemValue = NewItemValue;
}

// Item weight setter
void AFCItem::SetItemWeight(float NewItemWeight)
{
	ItemWeight = NewItemWeight;
}

// Use item function
void AFCItem::Use(AFCCharacter* Character)
{
	// This will be implemented in Blueprint
} 