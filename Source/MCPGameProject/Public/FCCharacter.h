// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Character.h"
#include "FCCharacter.generated.h"

UCLASS()
class MCPGAMEPROJECT_API AFCCharacter : public ACharacter
{
	GENERATED_BODY()

public:
	// Sets default values for this character's properties
	AFCCharacter();

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

	// Called for forwards/backward input
	void MoveForward(float Value);

	// Called for left/right input
	void MoveRight(float Value);

	// Called when jump is pressed
	void StartJump();

	// Called when jump is released
	void StopJump();

	// Called when sprint is pressed
	void StartSprint();

	// Called when sprint is released
	void StopSprint();

	// Called when interact is pressed
	void Interact();

	// Called when primary attack is pressed
	void PrimaryAttack();

	// Called when secondary action is pressed
	void SecondaryAction();

	// Update stress level based on lighting
	void UpdateStress();

	// Regenerate stamina over time
	void RegenerateStamina();

	// Consume stamina for actions
	void ConsumeStamina(float Amount);

	// Take damage and update health
	void TakeDamage(float DamageAmount);

	// Heal character
	void Heal(float HealAmount);

	// Pick up an item
	void PickUpItem(class AFCItem* Item);

	// Use an item from inventory
	void UseItem(class AFCItem* Item);

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;

	// Called to bind functionality to input
	virtual void SetupPlayerInputComponent(class UInputComponent* PlayerInputComponent) override;

	// Health getter and setter
	UFUNCTION(BlueprintCallable, Category = "Stats")
	float GetHealth() const { return Health; }

	UFUNCTION(BlueprintCallable, Category = "Stats")
	void SetHealth(float NewHealth);

	// Max health getter and setter
	UFUNCTION(BlueprintCallable, Category = "Stats")
	float GetMaxHealth() const { return MaxHealth; }

	UFUNCTION(BlueprintCallable, Category = "Stats")
	void SetMaxHealth(float NewMaxHealth);

	// Stamina getter and setter
	UFUNCTION(BlueprintCallable, Category = "Stats")
	float GetStamina() const { return Stamina; }

	UFUNCTION(BlueprintCallable, Category = "Stats")
	void SetStamina(float NewStamina);

	// Max stamina getter and setter
	UFUNCTION(BlueprintCallable, Category = "Stats")
	float GetMaxStamina() const { return MaxStamina; }

	UFUNCTION(BlueprintCallable, Category = "Stats")
	void SetMaxStamina(float NewMaxStamina);

	// Stress level getter and setter
	UFUNCTION(BlueprintCallable, Category = "Stats")
	float GetStressLevel() const { return StressLevel; }

	UFUNCTION(BlueprintCallable, Category = "Stats")
	void SetStressLevel(float NewStressLevel);

	// Movement speed getter and setter
	UFUNCTION(BlueprintCallable, Category = "Movement")
	float GetMovementSpeed() const { return MovementSpeed; }

	UFUNCTION(BlueprintCallable, Category = "Movement")
	void SetMovementSpeed(float NewMovementSpeed);

	// Sprint multiplier getter and setter
	UFUNCTION(BlueprintCallable, Category = "Movement")
	float GetSprintMultiplier() const { return SprintMultiplier; }

	UFUNCTION(BlueprintCallable, Category = "Movement")
	void SetSprintMultiplier(float NewSprintMultiplier);

	// Is sprinting getter
	UFUNCTION(BlueprintCallable, Category = "Movement")
	bool IsSprinting() const { return bIsSprinting; }

	// Is in light getter and setter
	UFUNCTION(BlueprintCallable, Category = "Environment")
	bool IsInLight() const { return bIsInLight; }

	UFUNCTION(BlueprintCallable, Category = "Environment")
	void SetInLight(bool InLight);

protected:
	// Character stats
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Stats")
	float Health;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Stats")
	float MaxHealth;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Stats")
	float Stamina;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Stats")
	float MaxStamina;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Stats")
	float StressLevel;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Stats")
	float MaxStressLevel;

	// Movement properties
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Movement")
	float MovementSpeed;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Movement")
	float SprintMultiplier;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Movement")
	float StaminaConsumptionRate;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Movement")
	float StaminaRegenerationRate;

	// Stress properties
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Stats")
	float StressIncreaseRate;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Stats")
	float StressDecreaseRate;

	// Environment properties
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Environment")
	bool bIsInLight;

	// Combat properties
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Combat")
	float AttackDamage;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Combat")
	float AttackStaminaCost;

	// Camera components
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Camera")
	class UCameraComponent* FirstPersonCamera;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Camera")
	class USpringArmComponent* SpringArm;

	// Mesh components
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Mesh")
	class USkeletalMeshComponent* ArmsMesh;

	// Inventory
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Inventory")
	TArray<class AFCItem*> Inventory;

	// Timers
	FTimerHandle StaminaRegenerationTimer;
	FTimerHandle StressUpdateTimer;

	// Flags
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Movement")
	bool bIsSprinting;
}; 