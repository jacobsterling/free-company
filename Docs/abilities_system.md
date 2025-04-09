# Abilities System Design

## Overview

The abilities system in Free Company is designed to provide each character class with unique and powerful skills that scale with their primary stats. Abilities can be swapped or randomized during mercenary employment, allowing for diverse character builds. The system emphasizes risk-reward mechanics, with many abilities having significant drawbacks or requiring careful positioning to avoid harming allies.

## Ability Categories

### Core Abilities
- Each class has 4-5 core abilities that define their playstyle
- Core abilities are available from level 1
- Abilities scale with relevant primary stats
- Cooldown and resource costs vary by ability
- Some abilities have area effects that can affect allies

### Specialization Abilities
- Unlocked at level 5 and 10
- Tied to character specialization paths
- More powerful than core abilities
- Often have significant drawbacks
- Can completely change a character's playstyle

### Experimental Abilities
- Discovered through experimentation
- Random effects and outcomes
- Can be powerful but unpredictable
- Often have humorous results
- Shared knowledge between players

## Class Abilities

### Warrior Abilities

#### Core Abilities
1. **Berserker Rage**
   - Description: Enter a rage state, increasing damage but reducing defense
   - Effect: +50% damage, -30% defense for 15 seconds
   - Cost: 30 stamina
   - Cooldown: 60 seconds
   - Scaling: Strength, Endurance
   - Visual: Character glows red, grows slightly larger

2. **Throw Ally**
   - Description: Pick up and throw an ally at enemies
   - Effect: Ally deals 100% weapon damage to enemies on impact
   - Cost: 25 stamina
   - Cooldown: 30 seconds
   - Scaling: Strength
   - Visual: Character picks up ally and hurls them

3. **Ground Slam**
   - Description: Slam the ground, creating a shockwave
   - Effect: Deals 75% weapon damage in a 5m radius, knocks back enemies
   - Cost: 20 stamina
   - Cooldown: 15 seconds
   - Scaling: Strength
   - Visual: Character jumps and slams weapon into ground

4. **Battle Cry**
   - Description: Let out a powerful shout that buffs allies
   - Effect: Allies within 10m gain +20% damage for 10 seconds
   - Cost: 15 stamina
   - Cooldown: 45 seconds
   - Scaling: Charisma
   - Visual: Character shouts with visible sound waves

#### Specialization Abilities (Berserker)
1. **Blood Frenzy**
   - Description: Damage dealt heals you for 30% of the amount
   - Effect: 30% life steal for 20 seconds
   - Cost: 40 stamina, 20% current health
   - Cooldown: 90 seconds
   - Scaling: Strength, Endurance
   - Visual: Character bleeds from wounds but attacks faster

#### Specialization Abilities (Craftsman)
1. **Weapon Mastery**
   - Description: Temporarily enhance your weapon
   - Effect: +30% weapon damage, +20% attack speed for 30 seconds
   - Cost: 25 stamina
   - Cooldown: 60 seconds
   - Scaling: Intelligence, Dexterity
   - Visual: Weapon glows with magical energy

### Rogue Abilities

#### Core Abilities
1. **Shadow Step**
   - Description: Become invisible for a short time
   - Effect: Invisibility for 5 seconds, next attack deals 150% damage
   - Cost: 25 stamina
   - Cooldown: 30 seconds
   - Scaling: Agility, Perception
   - Visual: Character fades into shadows

2. **Poison Strike**
   - Description: Apply poison to your weapon
   - Effect: Next 3 attacks apply poison that deals 20% weapon damage over 10 seconds
   - Cost: 15 stamina
   - Cooldown: 20 seconds
   - Scaling: Intelligence, Dexterity
   - Visual: Weapon drips with green poison

3. **Backstab**
   - Description: Deal increased damage from behind
   - Effect: 200% weapon damage when attacking from behind
   - Cost: 20 stamina
   - Cooldown: 10 seconds
   - Scaling: Dexterity, Agility
   - Visual: Character performs a quick stab animation

4. **Smoke Bomb**
   - Description: Create a smoke screen to escape
   - Effect: Creates a 5m smoke cloud, grants invisibility for 3 seconds
   - Cost: 30 stamina
   - Cooldown: 45 seconds
   - Scaling: Agility
   - Visual: Character throws a smoke bomb

#### Specialization Abilities (Assassin)
1. **Death Mark**
   - Description: Mark an enemy for death
   - Effect: Marked enemy takes 50% more damage from you for 15 seconds
   - Cost: 25 stamina
   - Cooldown: 60 seconds
   - Scaling: Dexterity, Perception
   - Visual: Red mark appears above enemy

#### Specialization Abilities (Alchemist)
1. **Toxic Cloud**
   - Description: Create a cloud of poison
   - Effect: 5m radius poison cloud that deals 30% weapon damage over 15 seconds
   - Cost: 35 stamina
   - Cooldown: 90 seconds
   - Scaling: Intelligence
   - Visual: Green poison cloud

### Mage Abilities

#### Core Abilities
1. **Frozen Earth**
   - Description: Freeze the ground, creating slippery terrain
   - Effect: Creates 8m radius of slippery ground, enemies take 20% weapon damage when falling
   - Cost: 30 mana
   - Cooldown: 25 seconds
   - Scaling: Intelligence
   - Visual: Ground freezes with ice crystals

2. **Firestorm**
   - Description: Create a massive fire tornado
   - Effect: 10m radius fire tornado that deals 80% spell damage over 8 seconds
   - Cost: 50 mana
   - Cooldown: 60 seconds
   - Scaling: Intelligence
   - Visual: Massive fire tornado

3. **Chain Lightning**
   - Description: Lightning that jumps between enemies
   - Effect: Deals 70% spell damage to primary target, 50% to 3 additional enemies
   - Cost: 25 mana
   - Cooldown: 15 seconds
   - Scaling: Intelligence
   - Visual: Lightning arcs between enemies

4. **Arcane Explosion**
   - Description: Create an explosion of arcane energy
   - Effect: 6m radius explosion dealing 100% spell damage, knocks back enemies
   - Cost: 40 mana
   - Cooldown: 30 seconds
   - Scaling: Intelligence
   - Visual: Purple explosion

#### Specialization Abilities (Elementalist)
1. **Elemental Storm**
   - Description: Summon a storm of all elements
   - Effect: 12m radius storm dealing 120% spell damage over 10 seconds
   - Cost: 60 mana, 20% current health
   - Cooldown: 120 seconds
   - Scaling: Intelligence, Endurance
   - Visual: Multi-colored storm

#### Specialization Abilities (Battlemage)
1. **Spell Blade**
   - Description: Enchant your weapon with magic
   - Effect: Weapon deals 50% additional spell damage for 20 seconds
   - Cost: 35 mana
   - Cooldown: 45 seconds
   - Scaling: Intelligence, Strength
   - Visual: Weapon glows with magical energy

### Priest Abilities

#### Core Abilities
1. **Blood Healing**
   - Description: Heal allies by sacrificing your own health
   - Effect: Heal target for 100% of damage taken from self
   - Cost: 20% current health
   - Cooldown: 10 seconds
   - Scaling: Faith, Self-Damage Efficiency
   - Visual: Character bleeds while healing target

2. **Holy Smite**
   - Description: Deal holy damage to enemies
   - Effect: Deals 80% weapon damage as holy damage
   - Cost: 15 stamina
   - Cooldown: 8 seconds
   - Scaling: Faith, Strength
   - Visual: Holy light strikes enemy

3. **Divine Shield**
   - Description: Create a protective barrier
   - Effect: Absorbs 200% faith in damage for 10 seconds
   - Cost: 30 stamina
   - Cooldown: 30 seconds
   - Scaling: Faith
   - Visual: Golden shield surrounds character

4. **Sacrificial Healing**
   - Description: Heal all allies by sacrificing health
   - Effect: Heal all allies within 10m for 50% of damage taken
   - Cost: 30% current health
   - Cooldown: 45 seconds
   - Scaling: Faith, Self-Damage Efficiency
   - Visual: Character bleeds while healing aura surrounds

#### Specialization Abilities (Martyr)
1. **Last Rites**
   - Description: Sacrifice yourself to heal allies
   - Effect: Heal all allies for 200% of your remaining health, you die
   - Cost: All remaining health
   - Cooldown: 180 seconds
   - Scaling: Faith, Self-Damage Efficiency
   - Visual: Character glows with holy light, then collapses

#### Specialization Abilities (Paladin)
1. **Holy Wrath**
   - Description: Enter a holy rage
   - Effect: +40% damage, +30% defense for 15 seconds
   - Cost: 40 stamina, 20% current health
   - Cooldown: 90 seconds
   - Scaling: Faith, Strength
   - Visual: Character glows with holy light, grows slightly larger

### Warlock Abilities

#### Core Abilities
1. **Summon Imp**
   - Description: Summon a small demon to fight for you
   - Effect: Summons an imp that deals 40% of your spell damage
   - Cost: 30 mana, 10% current health
   - Cooldown: 45 seconds
   - Scaling: Charisma, Summoning Power
   - Visual: Small imp appears from a portal

2. **Possess Enemy**
   - Description: Take control of an enemy
   - Effect: Control enemy for 10 seconds, they deal 50% of your spell damage
   - Cost: 40 mana, 20% current health
   - Cooldown: 60 seconds
   - Scaling: Charisma, Possession Control
   - Visual: Purple energy connects you to enemy

3. **Life Drain**
   - Description: Drain life from enemies to heal yourself
   - Effect: Deal 60% spell damage, heal for 50% of damage dealt
   - Cost: 25 mana
   - Cooldown: 15 seconds
   - Scaling: Intelligence, Faith
   - Visual: Purple energy drains from enemy to you

4. **Demon Pact**
   - Description: Make a pact with a demon for power
   - Effect: +50% spell damage, -30% health for 20 seconds
   - Cost: 30% current health
   - Cooldown: 90 seconds
   - Scaling: Charisma, Self-Damage Efficiency
   - Visual: Character is surrounded by demonic energy

#### Specialization Abilities (Summoner)
1. **Summon Greater Demon**
   - Description: Summon a powerful demon
   - Effect: Summons a demon that deals 100% of your spell damage
   - Cost: 50 mana, 30% current health
   - Cooldown: 120 seconds
   - Scaling: Charisma, Summoning Power
   - Visual: Large demon appears from a portal

#### Specialization Abilities (Possessor)
1. **Mass Possession**
   - Description: Possess multiple weak enemies
   - Effect: Control up to 3 weak enemies for 8 seconds
   - Cost: 60 mana, 40% current health
   - Cooldown: 180 seconds
   - Scaling: Charisma, Possession Control
   - Visual: Purple energy connects you to multiple enemies

### Ranger Abilities

#### Core Abilities
1. **Precise Shot**
   - Description: Fire a precise arrow
   - Effect: 150% weapon damage, guaranteed critical hit
   - Cost: 20 stamina
   - Cooldown: 15 seconds
   - Scaling: Dexterity, Perception
   - Visual: Arrow glows with energy

2. **Poison Trap**
   - Description: Set a trap that poisons enemies
   - Effect: Trap deals 40% weapon damage and applies poison for 15 seconds
   - Cost: 25 stamina
   - Cooldown: 30 seconds
   - Scaling: Intelligence, Dexterity
   - Visual: Trap glows green

3. **Animal Companion**
   - Description: Summon an animal to fight with you
   - Effect: Wolf deals 50% of your weapon damage
   - Cost: 30 stamina
   - Cooldown: 60 seconds
   - Scaling: Charisma, Summoning Power
   - Visual: Wolf appears and follows you

4. **Volley**
   - Description: Fire multiple arrows
   - Effect: Fire 5 arrows that deal 30% weapon damage each
   - Cost: 35 stamina
   - Cooldown: 25 seconds
   - Scaling: Dexterity, Agility
   - Visual: Character fires multiple arrows rapidly

#### Specialization Abilities (Archer)
1. **Rain of Arrows**
   - Description: Create a rain of arrows
   - Effect: 10m radius area takes 80% weapon damage over 5 seconds
   - Cost: 40 stamina
   - Cooldown: 60 seconds
   - Scaling: Dexterity, Perception
   - Visual: Arrows rain down from the sky

#### Specialization Abilities (Beastmaster)
1. **Pack Leader**
   - Description: Summon a pack of animals
   - Effect: Summon 3 wolves that deal 40% of your weapon damage each
   - Cost: 50 stamina
   - Cooldown: 120 seconds
   - Scaling: Charisma, Summoning Power
   - Visual: Multiple wolves appear

## Ability Scaling

### Primary Stat Scaling
- **Strength**: Physical damage, throwing distance, carrying capacity
- **Dexterity**: Accuracy, critical chance, attack speed
- **Intelligence**: Spell damage, crafting quality, trap effectiveness
- **Faith**: Healing power, holy damage, divine protection
- **Charisma**: Minion control, persuasion, leadership
- **Agility**: Movement speed, dodge chance, stealth effectiveness
- **Endurance**: Stamina pool, health regeneration, resistance to effects
- **Perception**: Detection range, trap finding, critical chance

### Derived Stat Scaling
- **Damage**: Base for all damaging abilities
- **Armor**: Reduces self-damage from abilities
- **Speed**: Affects ability cast time and movement during abilities
- **Critical Chance**: Affects critical hit abilities
- **Summoning Power**: Affects strength of summoned creatures
- **Possession Control**: Affects duration and control of possessed enemies
- **Self-Damage Efficiency**: Affects effectiveness of self-damaging abilities

## Ability Discovery

### Randomization
- Each mercenary gets 4-5 random abilities from their class pool
- Abilities can be swapped during level-up
- Specialization abilities are unlocked based on chosen path
- Experimental abilities are discovered through gameplay

### Documentation
- Players can document discovered ability combinations
- Knowledge sharing between players
- Ability effectiveness varies based on character stats
- Some abilities have hidden properties that are discovered through use

## Implementation Notes

### Technical Requirements
- Ability data structure with scaling formulas
- Cooldown and resource management system
- Visual and audio feedback for all abilities
- Effect application system
- Ability targeting system

### UI Considerations
- Clear ability icons with cooldown indicators
- Resource cost display
- Targeting indicators for area abilities
- Effect duration timers
- Ability tooltips with scaling information

### Balance Considerations
- Risk-reward balance for self-damaging abilities
- Area effect balance to encourage careful positioning
- Cooldown and resource cost balance
- Scaling formulas to ensure abilities remain effective at high levels
- Co-op balance to ensure abilities work well in team play 