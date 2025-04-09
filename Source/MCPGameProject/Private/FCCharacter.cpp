// Fill out your copyright notice in the Description page of Project Settings.

#include "FCCharacter.h"
#include "Camera/CameraComponent.h"
#include "Components/CapsuleComponent.h"
#include "Components/InputComponent.h"
#include "GameFramework/CharacterMovementComponent.h"
#include "GameFramework/Controller.h"
#include "GameFramework/SpringArmComponent.h"
#include "Kismet/GameplayStatics.h"
#include "Kismet/KismetMathLibrary.h"
#include "FCItem.h"

// Sets default values
AFCCharacter::AFCCharacter()
{
	// Set this character to call Tick() every frame
	PrimaryActorTick.bCanEverTick = true;

	// Set size for collision capsule
	GetCapsuleComponent()->InitCapsuleSize(42.f, 96.0f);

	// Set default values for character stats
	Health = 100.0f;
	MaxHealth = 100.0f;
	Stamina = 100.0f;
	MaxStamina = 100.0f;
	StressLevel = 0.0f;
	MaxStressLevel = 100.0f;

	// Set default values for movement
	MovementSpeed = 600.0f;
	SprintMultiplier = 1.5f;
	StaminaConsumptionRate = 10.0f;
	StaminaRegenerationRate = 5.0f;

	// Set default values for stress
	StressIncreaseRate = 5.0f;
	StressDecreaseRate = 3.0f;

	// Set default values for environment
	bIsInLight = false;

	// Set default values for combat
	AttackDamage = 10.0f;
	AttackStaminaCost = 15.0f;

	// Set default values for flags
	bIsSprinting = false;

	// Configure character movement
	GetCharacterMovement()->bOrientRotationToMovement = true;
	GetCharacterMovement()->RotationRate = FRotator(0.0f, 540.0f, 0.0f);
	GetCharacterMovement()->JumpZVelocity = 600.f;
	GetCharacterMovement()->AirControl = 0.2f;
	GetCharacterMovement()->MaxWalkSpeed = MovementSpeed;

	// Create camera component
	FirstPersonCamera = CreateDefaultSubobject<UCameraComponent>(TEXT("FirstPersonCamera"));
	FirstPersonCamera->SetupAttachment(GetCapsuleComponent());
	FirstPersonCamera->SetRelativeLocation(FVector(0.0f, 0.0f, 64.0f));
	FirstPersonCamera->bUsePawnControlRotation = true;

	// Create spring arm component
	SpringArm = CreateDefaultSubobject<USpringArmComponent>(TEXT("SpringArm"));
	SpringArm->SetupAttachment(GetCapsuleComponent());
	SpringArm->SetRelativeLocation(FVector(0.0f, 0.0f, 64.0f));
	SpringArm->TargetArmLength = 0.0f;
	SpringArm->bUsePawnControlRotation = true;

	// Create arms mesh component
	ArmsMesh = CreateDefaultSubobject<USkeletalMeshComponent>(TEXT("ArmsMesh"));
	ArmsMesh->SetupAttachment(FirstPersonCamera);
	ArmsMesh->SetRelativeLocation(FVector(0.0f, 0.0f, -10.0f));
	ArmsMesh->SetRelativeRotation(FRotator(0.0f, 0.0f, 0.0f));
	ArmsMesh->bOnlyVisibleOnOwningPlayer = true;
}

// Called when the game starts or when spawned
void AFCCharacter::BeginPlay()
{
	Super::BeginPlay();

	// Set initial movement speed
	GetCharacterMovement()->MaxWalkSpeed = MovementSpeed;

	// Start timers for stamina regeneration and stress update
	GetWorld()->GetTimerManager().SetTimer(StaminaRegenerationTimer, this, &AFCCharacter::RegenerateStamina, 1.0f, true);
	GetWorld()->GetTimerManager().SetTimer(StressUpdateTimer, this, &AFCCharacter::UpdateStress, 1.0f, true);
}

// Called every frame
void AFCCharacter::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

	// Update movement speed based on sprinting
	if (bIsSprinting && Stamina > 0.0f)
	{
		GetCharacterMovement()->MaxWalkSpeed = MovementSpeed * SprintMultiplier;
		ConsumeStamina(StaminaConsumptionRate * DeltaTime);
	}
	else
	{
		GetCharacterMovement()->MaxWalkSpeed = MovementSpeed;
	}
}

// Called to bind functionality to input
void AFCCharacter::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
	Super::SetupPlayerInputComponent(PlayerInputComponent);

	// Bind movement functions
	PlayerInputComponent->BindAxis("MoveForward", this, &AFCCharacter::MoveForward);
	PlayerInputComponent->BindAxis("MoveRight", this, &AFCCharacter::MoveRight);

	// Bind action functions
	PlayerInputComponent->BindAction("Jump", IE_Pressed, this, &AFCCharacter::StartJump);
	PlayerInputComponent->BindAction("Jump", IE_Released, this, &AFCCharacter::StopJump);
	PlayerInputComponent->BindAction("Sprint", IE_Pressed, this, &AFCCharacter::StartSprint);
	PlayerInputComponent->BindAction("Sprint", IE_Released, this, &AFCCharacter::StopSprint);
	PlayerInputComponent->BindAction("Interact", IE_Pressed, this, &AFCCharacter::Interact);
	PlayerInputComponent->BindAction("PrimaryAttack", IE_Pressed, this, &AFCCharacter::PrimaryAttack);
	PlayerInputComponent->BindAction("SecondaryAction", IE_Pressed, this, &AFCCharacter::SecondaryAction);

	// Bind rotation functions
	PlayerInputComponent->BindAxis("Turn", this, &APawn::AddControllerYawInput);
	PlayerInputComponent->BindAxis("LookUp", this, &APawn::AddControllerPitchInput);
}

// Called for forwards/backward input
void AFCCharacter::MoveForward(float Value)
{
	if ((Controller != nullptr) && (Value != 0.0f))
	{
		// Find out which way is forward
		const FRotator Rotation = Controller->GetControlRotation();
		const FRotator YawRotation(0, Rotation.Yaw, 0);

		// Get forward vector
		const FVector Direction = FRotationMatrix(YawRotation).GetUnitAxis(EAxis::X);
		AddMovementInput(Direction, Value);
	}
}

// Called for left/right input
void AFCCharacter::MoveRight(float Value)
{
	if ((Controller != nullptr) && (Value != 0.0f))
	{
		// Find out which way is right
		const FRotator Rotation = Controller->GetControlRotation();
		const FRotator YawRotation(0, Rotation.Yaw, 0);

		// Get right vector
		const FVector Direction = FRotationMatrix(YawRotation).GetUnitAxis(EAxis::Y);
		AddMovementInput(Direction, Value);
	}
}

// Called when jump is pressed
void AFCCharacter::StartJump()
{
	bPressedJump = true;
}

// Called when jump is released
void AFCCharacter::StopJump()
{
	bPressedJump = false;
}

// Called when sprint is pressed
void AFCCharacter::StartSprint()
{
	bIsSprinting = true;
}

// Called when sprint is released
void AFCCharacter::StopSprint()
{
	bIsSprinting = false;
}

// Called when interact is pressed
void AFCCharacter::Interact()
{
	// This will be implemented in Blueprint
}

// Called when primary attack is pressed
void AFCCharacter::PrimaryAttack()
{
	// Check if we have enough stamina
	if (Stamina >= AttackStaminaCost)
	{
		// Consume stamina
		ConsumeStamina(AttackStaminaCost);

		// This will be implemented in Blueprint
	}
}

// Called when secondary action is pressed
void AFCCharacter::SecondaryAction()
{
	// This will be implemented in Blueprint
}

// Update stress level based on lighting
void AFCCharacter::UpdateStress()
{
	if (bIsInLight)
	{
		// Decrease stress when in light
		SetStressLevel(FMath::Max(0.0f, StressLevel - StressDecreaseRate));
	}
	else
	{
		// Increase stress when in darkness
		SetStressLevel(FMath::Min(MaxStressLevel, StressLevel + StressIncreaseRate));
	}
}

// Regenerate stamina over time
void AFCCharacter::RegenerateStamina()
{
	if (!bIsSprinting)
	{
		// Regenerate stamina when not sprinting
		SetStamina(FMath::Min(MaxStamina, Stamina + StaminaRegenerationRate));
	}
}

// Consume stamina for actions
void AFCCharacter::ConsumeStamina(float Amount)
{
	SetStamina(FMath::Max(0.0f, Stamina - Amount));
}

// Take damage and update health
void AFCCharacter::TakeDamage(float DamageAmount)
{
	SetHealth(FMath::Max(0.0f, Health - DamageAmount));

	// Check if character is dead
	if (Health <= 0.0f)
	{
		// This will be implemented in Blueprint
	}
}

// Heal character
void AFCCharacter::Heal(float HealAmount)
{
	SetHealth(FMath::Min(MaxHealth, Health + HealAmount));
}

// Pick up an item
void AFCCharacter::PickUpItem(AFCItem* Item)
{
	if (Item)
	{
		Inventory.Add(Item);
		Item->SetOwner(this);
		Item->SetActorLocation(GetActorLocation());
		Item->SetActorHiddenInGame(true);
	}
}

// Use an item from inventory
void AFCCharacter::UseItem(AFCItem* Item)
{
	if (Item && Inventory.Contains(Item))
	{
		// This will be implemented in Blueprint
	}
}

// Health setter
void AFCCharacter::SetHealth(float NewHealth)
{
	Health = NewHealth;
}

// Max health setter
void AFCCharacter::SetMaxHealth(float NewMaxHealth)
{
	MaxHealth = NewMaxHealth;
}

// Stamina setter
void AFCCharacter::SetStamina(float NewStamina)
{
	Stamina = NewStamina;
}

// Max stamina setter
void AFCCharacter::SetMaxStamina(float NewMaxStamina)
{
	MaxStamina = NewMaxStamina;
}

// Stress level setter
void AFCCharacter::SetStressLevel(float NewStressLevel)
{
	StressLevel = NewStressLevel;
}

// Movement speed setter
void AFCCharacter::SetMovementSpeed(float NewMovementSpeed)
{
	MovementSpeed = NewMovementSpeed;
	GetCharacterMovement()->MaxWalkSpeed = MovementSpeed;
}

// Sprint multiplier setter
void AFCCharacter::SetSprintMultiplier(float NewSprintMultiplier)
{
	SprintMultiplier = NewSprintMultiplier;
}

// Is in light setter
void AFCCharacter::SetInLight(bool InLight)
{
	bIsInLight = InLight;
} 