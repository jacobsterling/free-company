# Enemy & Boss Design

## Overview

The enemy and boss system in Free Company is designed to create challenging and memorable encounters that test the player's skills and knowledge of the game's mechanics. Enemies are organized into classes that mirror player classes, with their own abilities and special attacks. Bosses are unique encounters with multiple phases and special mechanics that require specific strategies to overcome.

## Enemy Classes

### Warrior-Type Enemies
- **Bandit Warrior**
  - Base Stats: High health, medium damage, low speed
  - Resistances: High physical resistance, low magical resistance
  - Common Effects: Bleeding, Knockback
  - Special Abilities: Berserker Rage, Ground Slam
  - Behavior: Aggressive, charges at players
  - Appearance: Wears leather armor, wields a sword or axe

- **Orc Berserker**
  - Base Stats: Very high health, high damage, medium speed
  - Resistances: Very high physical resistance, medium magical resistance
  - Common Effects: Frenzy, Bleeding
  - Special Abilities: Blood Frenzy, Battle Cry
  - Behavior: Extremely aggressive, ignores pain
  - Appearance: Large green humanoid with tusks, minimal armor

### Rogue-Type Enemies
- **Goblin Scout**
  - Base Stats: Low health, medium damage, high speed
  - Resistances: Low physical resistance, medium magical resistance
  - Common Effects: Poison, Invisibility
  - Special Abilities: Shadow Step, Poison Strike
  - Behavior: Stealthy, attacks from behind
  - Appearance: Small green humanoid with leather armor

- **Dark Elf Assassin**
  - Base Stats: Medium health, high damage, very high speed
  - Resistances: Medium physical resistance, high magical resistance
  - Common Effects: Paranoia, Confusion
  - Special Abilities: Death Mark, Smoke Bomb
  - Behavior: Extremely stealthy, waits for the right moment
  - Appearance: Tall, dark-skinned elf with black leather armor

### Mage-Type Enemies
- **Cultist Mage**
  - Base Stats: Low health, high damage, medium speed
  - Resistances: Low physical resistance, high magical resistance
  - Common Effects: Frozen Ground, Fire
  - Special Abilities: Firestorm, Chain Lightning
  - Behavior: Keeps distance, casts spells from afar
  - Appearance: Hooded figure with glowing eyes

- **Lich Apprentice**
  - Base Stats: Medium health, very high damage, low speed
  - Resistances: Medium physical resistance, very high magical resistance
  - Common Effects: Blood Curse, Silenced
  - Special Abilities: Arcane Explosion, Elemental Storm
  - Behavior: Strategic, uses terrain to advantage
  - Appearance: Skeletal figure with glowing magical aura

### Priest-Type Enemies
- **Cult Priest**
  - Base Stats: Medium health, medium damage, medium speed
  - Resistances: Medium physical resistance, high holy resistance
  - Common Effects: Blood Healing, Holy Smite
  - Special Abilities: Sacrificial Healing, Divine Shield
  - Behavior: Supports other enemies, heals them
  - Appearance: Robed figure with holy symbols

- **Dark Priest**
  - Base Stats: High health, high damage, low speed
  - Resistances: High physical resistance, very high holy resistance
  - Common Effects: Blood Curse, Frenzy
  - Special Abilities: Last Rites, Holy Wrath
  - Behavior: Aggressive healer, damages self to heal allies
  - Appearance: Corrupted priest with dark aura

### Warlock-Type Enemies
- **Demon Cultist**
  - Base Stats: Medium health, high damage, medium speed
  - Resistances: Medium physical resistance, high possession resistance
  - Common Effects: Summon Imp, Life Drain
  - Special Abilities: Demon Pact, Summon Greater Demon
  - Behavior: Summons minions, drains life
  - Appearance: Robed figure with demonic symbols

- **Possessed Warrior**
  - Base Stats: High health, high damage, medium speed
  - Resistances: High physical resistance, high possession resistance
  - Common Effects: Possess Enemy, Mass Possession
  - Special Abilities: Demon Pact, Life Drain
  - Behavior: Controls other enemies, uses them as weapons
  - Appearance: Warrior with glowing purple eyes

### Ranger-Type Enemies
- **Goblin Archer**
  - Base Stats: Low health, medium damage, high speed
  - Resistances: Low physical resistance, medium environmental resistance
  - Common Effects: Precise Shot, Poison Trap
  - Special Abilities: Volley, Rain of Arrows
  - Behavior: Keeps distance, uses traps
  - Appearance: Small green humanoid with bow

- **Dark Elf Ranger**
  - Base Stats: Medium health, high damage, very high speed
  - Resistances: Medium physical resistance, high environmental resistance
  - Common Effects: Animal Companion, Poison Trap
  - Special Abilities: Pack Leader, Precise Shot
  - Behavior: Uses animals, sets traps
  - Appearance: Tall, dark-skinned elf with bow and animal companion

### Vampire-Type Enemies
- **Vampire Thrall**
  - Base Stats: Medium health, high damage, high speed
  - Resistances: High physical resistance, medium magical resistance, immune to mental effects
  - Common Effects: Blood Drain, Life Steal
  - Special Abilities: Bat Form, Blood Frenzy
  - Behavior: Aggressive, seeks to infect players
  - Appearance: Pale humanoid with fangs and red eyes

- **Blood Mage**
  - Base Stats: Low health, very high damage, medium speed
  - Resistances: Low physical resistance, very high magical resistance, immune to mental effects
  - Common Effects: Blood Curse, Hemorrhage
  - Special Abilities: Blood Storm, Life Tap
  - Behavior: Strategic, uses blood magic from afar
  - Appearance: Robed figure with blood-red aura

- **Vampire Knight**
  - Base Stats: Very high health, high damage, medium speed
  - Resistances: Very high physical resistance, high magical resistance, immune to mental effects
  - Common Effects: Blood Shield, Vampiric Strike
  - Special Abilities: Blood Armor, Bat Swarm
  - Behavior: Defensive, protects other vampires
  - Appearance: Armored knight with vampiric features

## Elite Enemies

Elite enemies are stronger versions of regular enemies with enhanced abilities and special modifiers.

### Elite Modifiers
1. **Champion**
   - Increased health and damage
   - Special visual effects
   - Unique ability variations
   - Drops better loot

2. **Cursed**
   - Applies negative effects to players
   - Resistant to certain damage types
   - Leaves behind harmful effects when killed
   - Drops cursed items

3. **Possessed**
   - Can control other enemies
   - Resistant to mental effects
   - Applies possession effects to players
   - Drops possession-related items

4. **Summoner**
   - Summons additional minions
   - Controls summoned creatures
   - Resistant to summoning effects
   - Drops summoning-related items

5. **Elemental**
   - Infused with elemental powers
   - Applies elemental effects to players
   - Resistant to corresponding element
   - Drops elemental items

## Boss Enemies

Bosses are unique encounters with multiple phases and special mechanics.

### Boss Types

1. **The Corrupted Knight**
   - Class: Warrior
   - Phases: 3 (Human, Corrupted, Demon)
   - Special Mechanics: 
     - Phase 1: Standard warrior abilities
     - Phase 2: Gains corruption abilities, self-damage for power
     - Phase 3: Transforms into demon, gains possession abilities
   - Weaknesses: Holy damage, light
   - Resistances: Physical damage, darkness
   - Drops: Knight's armor, corruption essence

2. **The Shadow Queen**
   - Class: Rogue/Mage hybrid
   - Phases: 3 (Stealth, Combat, Shadow)
   - Special Mechanics:
     - Phase 1: Invisible, sets traps
     - Phase 2: Reveals herself, uses poison and daggers
     - Phase 3: Transforms into shadow form, uses area effects
   - Weaknesses: Light damage, detection
   - Resistances: Stealth, poison
   - Drops: Shadow blade, queen's crown

3. **The Lich King**
   - Class: Mage/Warlock hybrid
   - Phases: 3 (Arcane, Necromancer, Lich)
   - Special Mechanics:
     - Phase 1: Uses arcane magic, creates hazards
     - Phase 2: Summons undead minions
     - Phase 3: Transforms into lich, uses life drain
   - Weaknesses: Holy damage, light
   - Resistances: Magic, undead
   - Drops: Lich's phylactery, king's staff

4. **The Blood Priest**
   - Class: Priest/Warlock hybrid
   - Phases: 3 (Healer, Blood Mage, Demon)
   - Special Mechanics:
     - Phase 1: Heals minions, uses holy magic
     - Phase 2: Uses blood magic, damages self for power
     - Phase 3: Transforms into demon, uses possession
   - Weaknesses: Holy damage, light
   - Resistances: Blood magic, possession
   - Drops: Blood amulet, priest's robes

5. **The Beast Lord**
   - Class: Ranger/Warrior hybrid
   - Phases: 3 (Hunter, Beast, Alpha)
   - Special Mechanics:
     - Phase 1: Uses bow and traps
     - Phase 2: Transforms into beast form, uses claws
     - Phase 3: Commands pack of beasts, uses area effects
   - Weaknesses: Fire, silver
   - Resistances: Physical damage, animal companions
   - Drops: Beast lord's fang, alpha's pelt

6. **The Vampire Lord**
   - Class: Vampire/Warrior/Mage hybrid
   - Phases: 3 (Noble, Beast, Ancient)
   - Special Mechanics:
     - Phase 1: Uses noble abilities, commands thralls
     - Phase 2: Transforms into bat-like creature, uses blood magic
     - Phase 3: Reveals true ancient form, uses powerful blood abilities
   - Weaknesses: Sunlight, holy damage, garlic
   - Resistances: Physical damage, darkness, blood magic
   - Drops: Vampire lord's fang, blood amulet, transformation scroll

### Boss Mechanics

1. **Phase Transitions**
   - Visual and audio cues indicate phase changes
   - Boss gains new abilities and resistances
   - Environment may change
   - Special effects during transition

2. **Environmental Hazards**
   - Boss-specific hazards that affect the arena
   - Can be used against the boss
   - May require specific positioning

3. **Minion Management**
   - Bosses may summon minions
   - Minions have specific roles
   - Some minions must be killed first
   - Minions may buff the boss

4. **Weak Point System**
   - Bosses have weak points that can be targeted
   - Weak points change between phases
   - Hitting weak points causes extra damage
   - Some weak points are only available at certain times

5. **Special Conditions**
   - Bosses may have special conditions that must be met
   - Some abilities only work under certain conditions
   - Players may need to trigger specific events
   - Environmental interactions may be required

## Enemy AI Behavior

### Basic Behaviors
1. **Aggressive**
   - Actively seeks out players
   - Attacks when in range
   - Pursues fleeing players
   - Uses offensive abilities frequently

2. **Defensive**
   - Maintains distance from players
   - Uses defensive abilities when health is low
   - Retreats when heavily damaged
   - Uses cover and positioning

3. **Support**
   - Stays behind other enemies
   - Buffs allies and debuffs players
   - Heals damaged allies
   - Uses utility abilities

4. **Ambush**
   - Hides until players are close
   - Attacks from stealth
   - Uses surprise abilities
   - Retreats to hide again

5. **Pack**
   - Coordinates with other enemies
   - Surrounds players
   - Uses flanking tactics
   - Shares buffs with allies

### Advanced Behaviors
1. **Adaptive**
   - Changes tactics based on player actions
   - Learns from player strategies
   - Counters repeated patterns
   - Develops resistance to frequently used abilities

2. **Terrain Awareness**
   - Uses terrain features for advantage
   - Avoids hazardous areas
   - Pushes players into hazards
   - Creates advantageous positions

3. **Resource Management**
   - Conserves powerful abilities
   - Uses basic attacks when resources are low
   - Saves healing for critical moments
   - Coordinates resource usage with allies

4. **Target Selection**
   - Prioritizes vulnerable players
   - Focuses on players with low health
   - Attacks isolated players
   - Targets players using powerful abilities

5. **Group Coordination**
   - Coordinates attacks with allies
   - Forms formations
   - Protects important allies
   - Shares information about player positions

## Enemy Progression

### Scaling
- Enemies scale with player level
- Higher-level enemies have more abilities
- Elite and boss enemies scale more dramatically
- Some enemies have fixed levels for challenge

### Variants
- Different visual appearances
- Varied ability combinations
- Unique effect modifiers
- Special loot tables

### Special Enemies
- Rare spawns with unique abilities
- Event-specific enemies
- Seasonal variants
- Challenge mode exclusives

## Implementation Notes

### Technical Requirements
- AI behavior trees for different enemy types
- Pathfinding and navigation systems
- Ability targeting and execution
- Effect application and management
- Boss phase transition system
- Enemy scaling formulas

### UI Considerations
- Health bars for enemies
- Effect indicators
- Boss phase indicators
- Weak point highlighting
- Ability telegraphs

### Balance Considerations
- Ensure enemies provide appropriate challenge
- Balance enemy abilities with player abilities
- Create meaningful choices in combat
- Maintain challenge while allowing for player skill
- Ensure boss encounters are memorable but beatable
- Balance co-op scaling for different player counts 