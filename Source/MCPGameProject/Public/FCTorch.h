// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "FCItem.h"
#include "FCTorch.generated.h"

UCLASS()
class MCPGAMEPROJECT_API AFCTorch : public AFCItem
{
	GENERATED_BODY()

public:
	// Sets default values for this actor's properties
	AFCTorch();

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

public:
	// Called every frame
	virtual void Tick(float DeltaTime) override;

	// Override Use function
	virtual void Use(class AFCCharacter* Character) override;

	// Toggle torch on/off
	UFUNCTION(BlueprintCallable, Category = "Torch")
	void ToggleTorch();

	// Get torch light component
	UFUNCTION(BlueprintCallable, Category = "Torch")
	class ULightComponent* GetTorchLight() const { return TorchLight; }

	// Get torch particle system
	UFUNCTION(BlueprintCallable, Category = "Torch")
	class UParticleSystemComponent* GetTorchParticleSystem() const { return TorchParticleSystem; }

	// Get fuel amount
	UFUNCTION(BlueprintCallable, Category = "Torch")
	float GetFuelAmount() const { return FuelAmount; }

	// Set fuel amount
	UFUNCTION(BlueprintCallable, Category = "Torch")
	void SetFuelAmount(float NewFuelAmount);

	// Get fuel consumption rate
	UFUNCTION(BlueprintCallable, Category = "Torch")
	float GetFuelConsumptionRate() const { return FuelConsumptionRate; }

	// Set fuel consumption rate
	UFUNCTION(BlueprintCallable, Category = "Torch")
	void SetFuelConsumptionRate(float NewFuelConsumptionRate);

	// Get light radius
	UFUNCTION(BlueprintCallable, Category = "Torch")
	float GetLightRadius() const { return LightRadius; }

	// Set light radius
	UFUNCTION(BlueprintCallable, Category = "Torch")
	void SetLightRadius(float NewLightRadius);

	// Get light intensity
	UFUNCTION(BlueprintCallable, Category = "Torch")
	float GetLightIntensity() const { return LightIntensity; }

	// Set light intensity
	UFUNCTION(BlueprintCallable, Category = "Torch")
	void SetLightIntensity(float NewLightIntensity);

	// Is torch lit
	UFUNCTION(BlueprintCallable, Category = "Torch")
	bool IsLit() const { return bIsLit; }

protected:
	// Consume fuel
	void ConsumeFuel(float DeltaTime);

	// Update light properties
	void UpdateLightProperties();

	// Torch components
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Torch")
	class ULightComponent* TorchLight;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Torch")
	class UParticleSystemComponent* TorchParticleSystem;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Torch")
	class UAudioComponent* TorchAudio;

	// Torch properties
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Torch")
	float FuelAmount;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Torch")
	float MaxFuelAmount;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Torch")
	float FuelConsumptionRate;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Torch")
	float LightRadius;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Torch")
	float LightIntensity;

	// Torch flags
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Torch")
	bool bIsLit;
}; 