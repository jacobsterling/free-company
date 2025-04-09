# Phase 1 Implementation Plan for Free Company

## Overview
This document outlines the implementation plan for Phase 1 of the Free Company game, focusing on core systems and the basic camp. Phase 1 will establish the foundation for the game, including the first-person character controller, basic combat, and the initial settlement.

## Implementation Steps

### 1. Project Setup and Structure (Day 1)
- [ ] Create necessary folders in Content directory:
  - Characters
  - Environments
  - Blueprints
  - Materials
  - Meshes
  - UI
  - VFX
- [ ] Set up basic project settings
- [ ] Configure input mappings for WASD, jumping, and interaction

### 2. First-Person Character Controller (Days 2-3)
- [ ] Create a basic first-person character blueprint
- [ ] Implement WASD movement
- [ ] Add jumping functionality
- [ ] Create a basic interaction system
- [ ] Implement sprinting
- [ ] Add basic collision detection
- [ ] Create a simple camera system with head bobbing

### 3. Basic Camp Environment (Days 4-5)
- [ ] Create a simple terrain for the camp
- [ ] Add trees and basic environment assets
- [ ] Create a campfire with lighting effects
- [ ] Build a basic tent
- [ ] Add ambient sounds (wind, fire crackling)
- [ ] Implement day/night cycle
- [ ] Create a simple skybox

### 4. Lighting System (Day 6)
- [ ] Implement dynamic lighting system
- [ ] Create torch blueprint with light component
- [ ] Add ability to place and pick up torches
- [ ] Implement light radius and intensity settings
- [ ] Create shadow casting for dynamic objects
- [ ] Add basic particle effects for the torch flame

### 5. Character Stats and Health System (Day 7)
- [ ] Create a character stats system
  - Health
  - Stamina
  - Basic attributes (strength, dexterity, etc.)
- [ ] Implement health regeneration
- [ ] Add stamina consumption for sprinting
- [ ] Create a simple UI for displaying stats
- [ ] Implement basic damage system

### 6. Basic Inventory System (Day 8)
- [ ] Create an inventory data structure
- [ ] Implement item pickup functionality
- [ ] Create a simple inventory UI
- [ ] Add ability to use/consume items
- [ ] Implement item stacking
- [ ] Create basic item categories (weapons, consumables, etc.)

### 7. Simple Combat System (Days 9-10)
- [ ] Create a basic weapon system
- [ ] Implement melee attack animations
- [ ] Add hit detection
- [ ] Create damage calculation
- [ ] Implement basic blocking/parrying
- [ ] Add weapon switching
- [ ] Create simple combat UI (health bars, stamina)

### 8. Basic Stress System (Day 11)
- [ ] Implement stress level tracking
- [ ] Create stress accumulation in darkness
- [ ] Add stress reduction in well-lit areas
- [ ] Implement visual effects for high stress
- [ ] Create a simple UI for displaying stress level
- [ ] Add basic stress-related gameplay effects

### 9. Integration and Testing (Day 12)
- [ ] Integrate all systems together
- [ ] Test gameplay loop
- [ ] Fix bugs and optimize performance
- [ ] Add basic game start/end conditions
- [ ] Create a simple tutorial or help system

## Technical Implementation Details

### Character Controller Blueprint
- Base class: `Character`
- Components:
  - Capsule Collider
  - First-person camera
  - Mesh (for arms/weapons)
- Input mappings:
  - WASD for movement
  - Space for jumping
  - Left Shift for sprinting
  - E for interaction
  - Left Mouse Button for primary attack
  - Right Mouse Button for secondary action

### Stats System
- Data structure for character stats
- Blueprint interface for stat modification
- Event system for stat changes
- UI elements for displaying stats

### Inventory System
- Data structure for items
- Blueprint interface for inventory management
- UI for displaying inventory
- Interaction system for picking up items

### Combat System
- Weapon data structure
- Attack animation system
- Hit detection using raycasts
- Damage calculation based on weapon and stats
- Combat UI elements

### Lighting System
- Dynamic light components
- Light radius and intensity settings
- Shadow casting
- Particle effects for light sources

### Stress System
- Stress level tracking
- Environmental factors affecting stress
- Visual and gameplay effects of stress
- UI for displaying stress level

## Blueprint Structure

### Character Blueprint
```
Character
├── Components
│   ├── Capsule Collider
│   ├── First-person Camera
│   ├── Mesh (for arms/weapons)
│   └── Spring Arm (for third-person view if needed)
├── Variables
│   ├── Health
│   ├── Max Health
│   ├── Stamina
│   ├── Max Stamina
│   ├── Stress Level
│   ├── Movement Speed
│   ├── Sprint Multiplier
│   └── Inventory
├── Functions
│   ├── Move
│   ├── Jump
│   ├── Sprint
│   ├── Interact
│   ├── Attack
│   ├── Take Damage
│   ├── Heal
│   ├── Consume Stamina
│   ├── Regenerate Stamina
│   ├── Update Stress
│   ├── Pick Up Item
│   └── Use Item
└── Events
    ├── On Take Damage
    ├── On Heal
    ├── On Stress Change
    └── On Inventory Change
```

### Campfire Blueprint
```
Actor
├── Components
│   ├── Mesh
│   ├── Light
│   ├── Particle System
│   └── Audio Source
├── Variables
│   ├── Light Radius
│   ├── Light Intensity
│   └── Stress Reduction Rate
└── Functions
    ├── Toggle
    └── Update Light Properties
```

### Torch Blueprint
```
Actor
├── Components
│   ├── Mesh
│   ├── Light
│   ├── Particle System
│   └── Audio Source
├── Variables
│   ├── Light Radius
│   ├── Light Intensity
│   ├── Fuel Amount
│   └── Fuel Consumption Rate
└── Functions
    ├── Toggle
    ├── Update Light Properties
    └── Consume Fuel
```

## Next Steps After Phase 1
Once Phase 1 is complete, we'll move on to Phase 2, which focuses on dungeon generation and exploration. This will build upon the foundation established in Phase 1, adding procedural dungeon generation, basic enemy AI, and resource gathering.

## Resources Needed
- Basic character model
- Simple weapon models
- Environment assets (trees, rocks, etc.)
- Campfire and torch models
- UI elements
- Sound effects
- Particle effects for fire and light sources 