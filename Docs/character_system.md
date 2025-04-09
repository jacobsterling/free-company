# Character System Design

## Overview

The character system in Free Company is designed to create deep, meaningful gameplay where each mercenary has unique strengths, weaknesses, and personalities. Players must carefully manage their team's physical and mental well-being while maximizing their effectiveness in both combat and settlement work. The system includes a comprehensive effects system that can create both hilarious and challenging situations, especially in co-op play.

## Character Creation & Hiring

### Hiring Process
- Mercenaries arrive at the player's settlement via a carriage
- Each arrival brings 3-5 potential recruits with randomized traits and skills
- Players can view detailed information about each mercenary before hiring
- Hiring costs vary based on experience, skills, and rarity
- Unhired mercenaries leave after a set time period

### Character Generation
- Each mercenary has a primary class that determines their combat role
- Secondary skills determine their effectiveness in settlement jobs
- Random traits add personality and gameplay variety
- Background stories provide context and potential quest hooks
- Visual customization options (limited to maintain distinct class appearances)
- Hidden properties that are discovered through experimentation
- Effect resistance and susceptibility profiles
- Random ability selection from class-specific ability pools

## Character Classes

### Combat Classes
1. **Warrior**
   - Melee specialist with high health and strength
   - Skills: Heavy weapons, throwing allies/enemies, berserker rage
   - Settlement role: Blacksmith, guard captain
   - Effect resistance: High resistance to physical effects, low resistance to mental effects
   - Specialization paths: Berserker (high damage, low defense) or Craftsman (balanced stats, crafting bonus)

2. **Rogue**
   - Stealth and poison specialist
   - Skills: Daggers, invisibility, poison application, trap disarming
   - Settlement role: Trader, scout
   - Effect resistance: High resistance to movement effects, low resistance to environmental effects
   - Specialization paths: Assassin (high burst damage) or Alchemist (poison crafting)

3. **Mage**
   - Spellcasting with area damage focus
   - Skills: Fire, ice, and lightning magic with environmental hazards
   - Settlement role: Enchanter, researcher
   - Effect resistance: High resistance to magical effects, low resistance to physical effects
   - Specialization paths: Elementalist (environmental hazards) or Battlemage (close-range spells)

4. **Ranger**
   - Ranged combat and tracking
   - Skills: Bows, animal handling, survival
   - Settlement role: Hunter, herbalist
   - Effect resistance: High resistance to environmental effects, low resistance to magical effects
   - Specialization paths: Archer (precise shots) or Beastmaster (animal companions)

5. **Priest**
   - Self-damaging healer and tank
   - Skills: Self-damage healing magic, buffs, holy weapons
   - Settlement role: Priest, healer
   - Effect resistance: High resistance to mental effects, low resistance to transformation effects
   - Specialization paths: Martyr (healing through self-damage) or Paladin (holy warrior)

6. **Warlock**
   - Summoner and possession specialist
   - Skills: Summoning minions, possessing enemies, self-damage abilities
   - Settlement role: Occultist, researcher
   - Effect resistance: High resistance to possession effects, low resistance to holy effects
   - Specialization paths: Summoner (minion control) or Possessor (enemy control)

### Settlement Classes
1. **Blacksmith**
   - Weapon and armor crafting
   - Skills: Metalworking, repair, quality control
   - Combat role: Warrior (secondary)
   - Effect resistance: High resistance to heat effects, low resistance to cold effects

2. **Alchemist**
   - Potion and reagent creation
   - Skills: Brewing, ingredient knowledge, experimentation
   - Combat role: Mage (secondary)
   - Effect resistance: High resistance to poison effects, low resistance to explosive effects

3. **Innkeeper**
   - Food preparation and morale management
   - Skills: Cooking, hospitality, gossip
   - Combat role: Cleric (secondary)
   - Effect resistance: High resistance to social effects, low resistance to isolation effects

4. **Merchant**
   - Trading and resource management
   - Skills: Negotiation, appraisal, market knowledge
   - Combat role: Rogue (secondary)
   - Effect resistance: High resistance to economic effects, low resistance to combat effects

5. **Scout**
   - Exploration and resource gathering
   - Skills: Navigation, foraging, stealth
   - Combat role: Ranger (secondary)
   - Effect resistance: High resistance to navigation effects, low resistance to combat effects

## Character Stats

### Primary Stats
1. **Health** - Determines survivability in combat
2. **Stamina** - Limits ability usage and movement
3. **Strength** - Affects physical damage and carrying capacity
4. **Dexterity** - Affects accuracy, dodge chance, and lockpicking
5. **Intelligence** - Affects spell power and crafting quality
6. **Faith** - Affects healing power and holy magic effectiveness
7. **Charisma** - Affects persuasion and minion control
8. **Agility** - Affects movement speed and dodge chance
9. **Endurance** - Affects stamina pool and regeneration
10. **Perception** - Affects detection of traps and hidden items

### Derived Stats
1. **Damage** - Calculated from primary stats and equipment
2. **Armor** - Reduces incoming damage
3. **Speed** - Affects movement rate and action order
4. **Critical Chance** - Probability of dealing critical hits
5. **Stress Resistance** - How well a character handles stress
6. **Work Efficiency** - How effectively a character performs settlement tasks
7. **Effect Resistance** - How well a character resists various effect types
8. **Summoning Power** - Affects the strength of summoned creatures
9. **Possession Control** - Affects the effectiveness of possession abilities
10. **Self-Damage Efficiency** - Affects the effectiveness of self-damage abilities

## Mental State System

### Stress Levels
- Characters accumulate stress during dangerous situations
- High stress leads to negative traits and behaviors
- Stress can be reduced through rest, entertainment, and positive experiences
- Extreme stress can lead to permanent mental afflictions
- Experimental treatments can temporarily modify stress levels

### Mental Traits
- **Virtues**: Positive traits that appear under stress (e.g., Courageous, Focused)
- **Afflictions**: Negative traits that appear under stress (e.g., Paranoid, Abusive)
- Traits affect both combat performance and settlement behavior
- Some traits can be permanent if not treated
- Experimental effects can temporarily add or remove traits

### Relationship System
- Characters form relationships with each other
- Positive relationships provide stress relief and combat bonuses
- Negative relationships increase stress and can lead to conflicts
- Relationships evolve based on shared experiences and interactions
- Experimental effects can temporarily modify relationships

## Character Progression

### Experience & Leveling
- Characters gain experience from combat and successful work
- Leveling increases primary stats and unlocks new abilities
- Higher levels require more experience to advance
- Maximum level is 20, with significant power increases at key levels
- Experimental effects can temporarily boost or reduce experience gain

### Skill Development
- Skills improve through use in both combat and settlement
- Specialized training can accelerate skill growth
- Some skills have prerequisites or class restrictions
- Mastery of skills unlocks special abilities and bonuses
- Experimental effects can temporarily boost or reduce skill effectiveness

### Equipment & Loadout
- Characters can equip weapons, armor, and accessories
- Equipment affects stats and provides special abilities
- Weight system limits how much can be carried
- Equipment can be crafted, found, or purchased
- Enchanted equipment can have unexpected effects

## Character Management

### Daily Routines
- Characters need food, rest, and entertainment
- Work schedules can be assigned in the settlement
- Downtime activities help reduce stress
- Special events can interrupt normal routines
- Experimental food and potions can modify daily needs

### Injuries & Recovery
- Characters can be injured in combat
- Injuries reduce effectiveness and require healing
- Some injuries may be permanent
- Medical facilities in the settlement aid recovery
- Experimental treatments can have unexpected results

### Death & Replacement
- Characters who die in combat cannot be revived
- Death affects the morale of surviving characters
- New mercenaries must be hired to replace the fallen
- Memorials can be built to honor fallen comrades
- Experimental effects can temporarily prevent death

## Effects System Integration

### Physical Effects
1. **Movement Effects**
   - Blindness: Complete loss of vision
   - Tunnel Vision: Reduced field of view
   - Knockback: Pushed in a direction
   - Zero Gravity: Reduced gravity effect
   - Vomiting: Intermittent movement interruption

2. **Combat Effects**
   - Frenzy: Uncontrollably attack nearest target (friend or foe)
   - Bleeding: Continuous health loss
   - Broken Legs: Reduced movement speed
   - Broken Arms: Reduced attack effectiveness
   - Concussions: Reduced mana regeneration

3. **Special Effects**
   - Blood Curse: Healing deals damage instead
   - Silenced: Cannot use abilities
   - Chicken Form: Transformed into a chicken (limited abilities)
   - Knockback: Pushed in a direction
   - Zero Gravity: Reduced gravity effect

### Mental Effects
1. **Perception Effects**
   - Paranoia: Distrust of allies
   - Tunnel Vision: Reduced field of view
   - Light Sensitivity: Discomfort in bright light
   - Night Vision: Enhanced vision in darkness
   - Blindness: Complete loss of vision

2. **Behavior Effects**
   - Frenzy: Uncontrollably attack nearest target
   - Confusion: Random actions
   - Focus: Improved concentration
   - Distraction: Reduced attention span
   - Obsession: Fixation on specific targets

3. **Environmental Effects**
   - Frozen Ground: Slippery movement
   - Fire: Continuous fire damage
   - Poison Cloud: Poison damage over time
   - Electricity: Shock damage and stunning
   - Acid: Armor reduction and damage

### Effect Management
- Track all active effects on characters
- Manage effect interactions and conflicts
- Handle unexpected combinations
- Document new discoveries
- Share knowledge with team members

## Co-op Interactions

### Character Sharing
- Players can share control of characters
- Assign specific characters to different players
- Collaborative character management
- Shared progression and development
- Team-based decision making

### Experimental Collaboration
- Work together to discover new recipes
- Share knowledge about effects and interactions
- Collaborative problem solving for negative effects
- Competitive challenges using experimental effects
- Team-based experimentation for better results

### Social Dynamics
- Inter-player relationships affect gameplay
- Collaborative or competitive goals
- Shared settlement management
- Team-based challenges and achievements
- Role-playing opportunities

## Implementation Notes

### Technical Requirements
- Character data structure to store all stats and traits
- AI system for autonomous behavior in settlement
- State machine for character status and behaviors
- Save/load system for character persistence
- Effect tracking and management system
- Co-op synchronization and networking

### UI Considerations
- Character sheet showing all stats and traits
- Status indicators for health, stress, and other conditions
- Inventory management interface
- Skill tree visualization
- Relationship network display
- Effect status and management interface
- Co-op interaction tools
- Simple, clear visual indicators for effects

### Balance Considerations
- Ensure no single class or build is dominant
- Balance combat effectiveness with settlement utility
- Create meaningful choices in character development
- Maintain challenge while allowing for player creativity
- Balance experimental effects for fun without breaking gameplay
- Ensure co-op play is balanced and enjoyable
- Balance effect potency with duration and frequency

## Vampirism System

### Infection Process
- Contracted from vampire attacks
- Transmitted through blood pools
- Curable with specific items
- Permanent if not treated quickly
- Special vampire hunter abilities to cure

### Transformation Stages
1. **Stage 1: Minor Symptoms**
   - Enhanced night vision
   - Slight sunlight sensitivity
   - No significant changes to gameplay
   - Curable with basic remedies

2. **Stage 2: Blood Hunger**
   - Blood hunger begins
   - Increased sunlight vulnerability
   - Requires blood consumption
   - Curable with advanced remedies

3. **Stage 3: Full Transformation**
   - Can transform into bat form
   - Severe sunlight vulnerability
   - Blood replaces food requirements
   - Only curable with rare items

4. **Stage 4: Irreversible**
   - Complete vampire transformation
   - Permanent condition
   - Full vampire abilities
   - Cannot be cured

### Vampire Abilities
1. **Blood Consumption**
   - Heals health
   - Replaces food requirements
   - Can be collected from enemies or allies
   - Different blood types have different effects

2. **Bat Form**
   - Transform into a bat
   - Flight capability
   - Enhanced speed
   - Limited combat abilities

3. **Night Vision**
   - See clearly in darkness
   - Enhanced perception
   - Detect heat signatures
   - Track blood trails

4. **Life Steal**
   - Drain life from enemies
   - Heal while dealing damage
   - Transfer health to allies
   - Create blood pools

5. **Blood Magic**
   - Cast spells using blood
   - Create blood constructs
   - Control blood flow
   - Enhance other abilities

### Settlement Integration
1. **Vampire Quarters**
   - Special sleeping areas
   - Sunlight protection
   - Blood storage
   - Bat roosts

2. **Blood Supply Management**
   - Collect and store blood
   - Distribute to vampire members
   - Maintain fresh supply
   - Special preservation methods

3. **Night Shift Assignments**
   - Assign vampires to night work
   - Protect settlement at night
   - Gather resources in darkness
   - Special night-only tasks

4. **Sunlight Protection**
   - Create shaded areas
   - Provide protective gear
   - Schedule activities around daylight
   - Emergency protection measures 