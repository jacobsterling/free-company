#include "FCTorch.h"
#include "FCCharacter.h"
#include "Components/LightComponent.h"
#include "Components/ParticleSystemComponent.h"
#include "Components/AudioComponent.h"

// Sets default values
AFCTorch::AFCTorch()
{
	// Set this actor to call Tick() every frame
	PrimaryActorTick.bCanEverTick = true;

	// Create torch components
	TorchLight = CreateDefaultSubobject<ULightComponent>(TEXT("TorchLight"));
	TorchLight->SetupAttachment(RootComponent);
	TorchLight->SetVisibility(false);

	TorchParticleSystem = CreateDefaultSubobject<UParticleSystemComponent>(TEXT("TorchParticleSystem"));
	TorchParticleSystem->SetupAttachment(RootComponent);
	TorchParticleSystem->SetVisibility(false);

	TorchAudio = CreateDefaultSubobject<UAudioComponent>(TEXT("TorchAudio"));
	TorchAudio->SetupAttachment(RootComponent);

	// Set default torch properties
	FuelAmount = 100.0f;
	MaxFuelAmount = 100.0f;
	FuelConsumptionRate = 1.0f;
	LightRadius = 500.0f;
	LightIntensity = 5000.0f;
	bIsLit = false;

	// Set item properties
	SetItemName(TEXT("Torch"));
	SetItemDescription(TEXT("A simple torch that provides light and warmth."));
	SetItemType(EItemType::Torch);
	SetItemValue(10);
	SetItemWeight(1.0f);
}

// Called when the game starts or when spawned
void AFCTorch::BeginPlay()
{
	Super::BeginPlay();

	// Set initial light properties
	TorchLight->SetIntensity(LightIntensity);
	TorchLight->SetAttenuationRadius(LightRadius);
}

// Called every frame
void AFCTorch::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

	// Consume fuel if torch is lit
	if (bIsLit)
	{
		ConsumeFuel(DeltaTime);
	}
}

void AFCTorch::Use(AFCCharacter* Character)
{
	if (Character)
	{
		// Toggle torch when used
		ToggleTorch();
	}
}

void AFCTorch::ToggleTorch()
{
	bIsLit = !bIsLit;

	// Update visibility and effects
	TorchLight->SetVisibility(bIsLit);
	TorchParticleSystem->SetVisibility(bIsLit);

	if (bIsLit)
	{
		// Play torch sound
		if (TorchAudio)
		{
			TorchAudio->Play();
		}
	}
	else
	{
		// Stop torch sound
		if (TorchAudio)
		{
			TorchAudio->Stop();
		}
	}
}

void AFCTorch::ConsumeFuel(float DeltaTime)
{
	// Consume fuel over time
	FuelAmount = FMath::Max(0.0f, FuelAmount - (FuelConsumptionRate * DeltaTime));

	// Update light properties based on fuel
	UpdateLightProperties();

	// Extinguish torch if out of fuel
	if (FuelAmount <= 0.0f)
	{
		bIsLit = false;
		TorchLight->SetVisibility(false);
		TorchParticleSystem->SetVisibility(false);
		if (TorchAudio)
		{
			TorchAudio->Stop();
		}
	}
}

void AFCTorch::UpdateLightProperties()
{
	// Calculate light intensity based on fuel amount
	float FuelRatio = FuelAmount / MaxFuelAmount;
	float CurrentIntensity = LightIntensity * FuelRatio;
	TorchLight->SetIntensity(CurrentIntensity);
}

void AFCTorch::SetFuelAmount(float NewFuelAmount)
{
	FuelAmount = FMath::Clamp(NewFuelAmount, 0.0f, MaxFuelAmount);
	UpdateLightProperties();
}

void AFCTorch::SetFuelConsumptionRate(float NewFuelConsumptionRate)
{
	FuelConsumptionRate = NewFuelConsumptionRate;
}

void AFCTorch::SetLightRadius(float NewLightRadius)
{
	LightRadius = NewLightRadius;
	TorchLight->SetAttenuationRadius(LightRadius);
}

void AFCTorch::SetLightIntensity(float NewLightIntensity)
{
	LightIntensity = NewLightIntensity;
	UpdateLightProperties();
} 