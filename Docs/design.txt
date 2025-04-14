# Free Company - Game Design Document

## Game Concept

**Free Company** is a hardcore first-person dungeon crawler that combines the strategic depth of "Darkest Dungeon" with the settlement management of "RimWorld" and the visual style of "Schedule 1". Players manage a band of mercenaries, exploring dangerous dungeons while developing a home base from a simple camp into a thriving town. The game features experimental crafting systems that encourage discovery and experimentation, with both hilarious and potentially game-changing results, especially in co-op play. The game uses a simple, stylized graphics approach to focus on gameplay depth rather than visual fidelity.

## Core Gameplay Loop

1. **Exploration & Combat**: Venture into procedurally generated dungeons in first-person view
2. **Resource Gathering**: Collect gold, materials, and rare items from dungeons
3. **Base Building**: Return to your settlement to upgrade facilities and hire new mercenaries
4. **Character Management**: Maintain the physical and mental health of your mercenaries
5. **Experimentation**: Discover new recipes and effects through trial and error
6. **Progression**: Unlock new abilities, equipment, and settlement upgrades

## Core Mechanics

### First-Person Dungeon Crawling
- WASD movement with jumping and sprinting
- First-person combat with melee and ranged weapons
- Procedurally generated dungeons with different themes and monster types
- Resource gathering and treasure hunting
- Dynamic lighting system with torches and other light sources
- Darkness increases stress levels, requiring light management
- Push-to-talk voice chat with proximity-based communication
- Voice chat affected by mental effects (paranoia, deafness, etc.)

### Character Management
- Each mercenary has unique classes and skills
- Dual-purpose characters: combat specialists who can also work in the settlement
- Health, stamina, and stress management systems
- Mental state system similar to Darkest Dungeon
- Permadeath: fallen mercenaries must be replaced
- Comprehensive effects system for physical, mental, and environmental conditions
- Risk-reward abilities that can damage the user or allies
- AI-controlled mercenaries when not directly controlled by players

### Settlement Building
- Start with a basic camp (campfire, tent, trees)
- Upgrade to a full town with multiple buildings
- Buildings provide services and crafting capabilities
- Assign workers to different posts (tavern, blacksmith, etc.)
- Resource management and production chains

### Experimental Systems
- Alchemy system with hidden ingredient properties
- Enchanting system with unexpected interactions
- Medical system for treating physical and mental afflictions
- Effect system tracking all active effects and their interactions
- Discovery-based progression through experimentation

### Co-op Features
- Play with friends in shared dungeons and settlement
- Collaborative experimentation and discovery
- Share knowledge and recipes
- Competitive challenges and pranks
- Team-based problem solving
- Proximity-based voice chat with effect interactions

## Development Roadmap

### Phase 1: Core Systems & Basic Camp
- [ ] First-person character controller with basic movement
- [ ] Simple combat system
- [ ] Basic camp with campfire and tent
- [ ] Character stats and health system
- [ ] Basic inventory system
- [ ] Simple lighting system with torches
- [ ] Basic stress system tied to lighting

### Phase 2: Dungeon Generation & Exploration
- [ ] Procedural dungeon generation
- [ ] Basic enemy AI and combat
- [ ] Resource gathering in dungeons
- [ ] Simple loot system
- [ ] Return to camp mechanics
- [ ] Basic environmental effects
- [ ] Darkness and lighting effects on stress

### Phase 3: Character Management & Progression
- [ ] Character classes and skills
- [ ] Stress and mental state system
- [ ] Character hiring from carriage
- [ ] Basic character progression
- [ ] Food and resource consumption
- [ ] Basic effect system implementation
- [ ] Core abilities for each class
- [ ] AI control for unassigned mercenaries

### Phase 4: Settlement Expansion
- [ ] Building placement system
- [ ] Basic building types (tavern, blacksmith)
- [ ] Worker assignment system
- [ ] Resource production
- [ ] Town upgrade paths

### Phase 5: Experimental Systems
- [ ] Basic alchemy system
- [ ] Simple enchanting mechanics
- [ ] Medical treatment system
- [ ] Effect tracking and management
- [ ] Discovery documentation
- [ ] Advanced effect interactions
- [ ] Specialization abilities

### Phase 6: Co-op Implementation
- [ ] Multiplayer networking
- [ ] Shared settlement mechanics
- [ ] Collaborative experimentation
- [ ] Team-based challenges
- [ ] Knowledge sharing systems
- [ ] Proximity-based voice chat
- [ ] Voice chat effect interactions

### Phase 7: Advanced Systems
- [ ] Advanced crafting systems
- [ ] Complex enemy types and bosses
- [ ] Special events and quests
- [ ] Advanced settlement management
- [ ] End-game content
- [ ] Full effects system implementation
- [ ] Experimental abilities
- [ ] Advanced AI behaviors

## Technical Design

### Game Engine
- Unreal Engine 5
- Python scripting for game logic
- Modular architecture for easy expansion

### Key Systems
1. **Character System**
   - Stats, skills, and progression
   - Mental and physical state management
   - Class-based abilities
   - Effect resistance and susceptibility
   - Risk-reward ability mechanics
   - AI control for unassigned mercenaries

2. **Combat System**
   - First-person melee and ranged combat
   - Enemy AI and behavior patterns
   - Damage calculation and effects
   - Status effect application and management
   - Area effect hazards that can affect allies
   - Enemy classes with player-like abilities

3. **Settlement System**
   - Building placement and management
   - Resource production and consumption
   - Worker assignment and efficiency
   - Environmental effect management

4. **Dungeon Generation**
   - Procedural level creation
   - Theme-based environments
   - Loot and reward distribution
   - Environmental hazard placement
   - Dungeon-specific enemy types and modifiers
   - Specialized loot and ingredients

5. **Economy System**
   - Resource gathering and crafting
   - Mercenary hiring and management
   - Building upgrades and maintenance
   - Effect-based economy modifiers

6. **Experimental Systems**
   - Alchemy and potion crafting
   - Weapon and armor enchanting
   - Medical treatment and healing
   - Effect tracking and management
   - Discovery and documentation

7. **Effects System**
   - Physical effects (movement, combat, injuries)
   - Mental effects (perception, personality)
   - Environmental effects (weather, terrain)
   - Transformation effects (polymorphism, size)
   - Magical effects (elemental, arcane)
   - Experimental effects (alchemical, enchantment)
   - Voice chat interaction effects

8. **Abilities System**
   - Class-specific abilities with unique mechanics
   - Risk-reward abilities that can damage the user
   - Area effect abilities that can affect allies
   - Ability scaling with character stats
   - Specialization paths for each class
   - Experimental abilities discovered through gameplay

9. **Enemy & Boss System**
   - Enemy classes with player-like abilities
   - Boss mechanics and phases
   - Resistance profiles and weaknesses
   - Effect application to players
   - Special abilities and attacks
   - AI behavior patterns

10. **Level Design System**
    - Dungeon themes and environments
    - Enemy type distribution
    - Special loot and ingredients
    - Environmental hazards
    - Boss encounters
    - Effect modifiers

11. **Co-op Systems**
    - Multiplayer networking
    - Shared progression
    - Collaborative gameplay
    - Knowledge sharing
    - Team challenges
    - Proximity-based voice chat

## Art Style & Visual Direction

- Simple, stylized graphics focusing on gameplay over visual fidelity
- Low-poly models with distinctive silhouettes
- Limited color palette with high contrast
- Procedural textures for variety
- Particle effects for important gameplay elements
- Dynamic lighting with emphasis on torch-based illumination
- Visual feedback for all effects and status changes
- Minimal UI that doesn't obstruct gameplay
- Distinctive visual language for different effect types
- Atmospheric lighting that affects player stress

## Related Documents

- [Character System Design](character_system.md)
- [Combat Mechanics](combat_mechanics.md)
- [Settlement Building](settlement_building.md)
- [Dungeon Generation](dungeon_generation.md)
- [Economy System](economy_system.md)
- [Experimental Systems](experimental_systems.md)
- [Effects System](effects_system.md)
- [Abilities System](abilities_system.md)
- [Enemy & Boss Design](enemy_boss_design.md)
- [Level Design](level_design.md)
- [AI Systems](ai_systems.md)
- [Voice Chat & Communication](voice_chat_system.md)

## Current Focus

Our immediate focus is implementing the basic camp and first-person character controller:

1. Create a starting camp with:
   - Campfire
   - One tent
   - Some trees
   - Basic environment
   - Simple lighting system

2. Implement first-person camera with:
   - WASD movement
   - Jumping
   - Basic interaction system
   - Torch mechanics

This foundation will allow us to build upon these core systems as we progress through the development roadmap.
