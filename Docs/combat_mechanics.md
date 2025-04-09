# Combat Mechanics Design

## Overview

The combat system in Free Company combines first-person action with strategic elements, requiring players to manage resources and positioning in real-time. Combat is further enhanced by a comprehensive effects system that can create both challenging and humorous situations, especially in co-op play.

## First-Person Combat

### Movement & Positioning
- WASD movement with sprint and crouch options
- Jump and dodge mechanics for evasive maneuvers
- Stamina management for sustained movement
- Cover system for tactical positioning
- Experimental effects can modify movement:
  - Blindness: Complete loss of vision
  - Tunnel Vision: Reduced field of view
  - Knockback: Pushed in a direction
  - Zero Gravity: Reduced gravity effect
  - Vomiting: Intermittent movement interruption

### Combat Controls
- Left click for primary attack
- Right click for block/parry
- Q/E for weapon switching
- R for reload
- F for interaction
- Space for dodge
- Shift for sprint
- Experimental effects can remap controls:
  - Confusion: Random control mapping
  - Frenzy: Automatic attacks
  - Focus: Enhanced precision
  - Distraction: Delayed responses
  - Obsession: Locked on target

### Weapon Types
1. **Melee Weapons**
   - Swords: Balanced damage and speed
   - Axes: High damage, slow speed
   - Daggers: Fast attacks, low damage
   - Spears: Long range, medium damage
   - Experimental weapons with random effects

2. **Ranged Weapons**
   - Bows: Silent, reusable ammunition
   - Crossbows: High damage, slow reload
   - Throwing weapons: Quick use, limited ammo
   - Experimental weapons with personality

3. **Magical Weapons**
   - Staves: Channeled spells
   - Wands: Quick cast spells
   - Tomes: Complex spell combinations
   - Experimental weapons with chaotic results

### Combat Abilities
- Class-specific abilities
- Weapon-specific moves
- Environmental interactions
- Experimental abilities with unexpected effects
- Co-op combo attacks

### Feedback Systems
- Visual damage indicators
- Audio cues for hits and blocks
- Screen effects for status changes
- Experimental effect visualizations:
  - Blindness: Black screen
  - Tunnel Vision: Vignette effect
  - Frenzy: Red tint
  - Confusion: Screen distortion
  - Zero Gravity: Floating particles

## Enemy System

### Enemy Types
1. **Common Enemies**
   - Basic combat abilities
   - Predictable patterns
   - Weak to specific tactics
   - Can be affected by experimental effects

2. **Elite Enemies**
   - Enhanced abilities
   - Special attacks
   - Resistance to certain effects
   - Can apply experimental effects

3. **Boss Enemies**
   - Unique mechanics
   - Multiple phases
   - Environmental interactions
   - Can create experimental situations

### Enemy AI
- Pathfinding and navigation
- Target selection and priority
- Attack patterns and timing
- Response to player actions
- Adaptation to experimental effects

### Enemy Progression
- Scaling difficulty
- New abilities and patterns
- Enhanced resistances
- Experimental variations
- Co-op specific challenges

## Combat Mechanics

### Damage System
- Base damage calculation
- Critical hits and multipliers
- Armor and resistance
- Status effect modifiers
- Experimental damage types:
  - Blood Curse: Healing deals damage
  - Frenzy: Increased damage to all targets
  - Confusion: Random damage values
  - Focus: Precise critical hits
  - Obsession: Increased damage to target

### Health & Healing
- Health pool management
- Healing items and spells
- Regeneration mechanics
- Experimental healing effects:
  - Vomiting: Intermittent healing
  - Blood Curse: Healing hurts
  - Frenzy: Life steal
  - Focus: Enhanced healing
  - Obsession: Target-based healing

### Stamina & Mana
- Resource management
- Regeneration rates
- Cost calculations
- Experimental resource effects:
  - Concussions: Reduced mana regen
  - Frenzy: Unlimited stamina
  - Confusion: Random costs
  - Focus: Efficient resource use
  - Obsession: Target-based costs

### Status Effects
- Duration tracking
- Stack management
- Interaction rules
- Experimental status effects:
  - Broken Limbs: Movement/attack penalties
  - Blood Curse: Healing reversal
  - Frenzy: Uncontrolled attacks
  - Confusion: Random actions
  - Chicken Form: Limited abilities

## Combat Environment

### Dungeon Hazards
- Traps and pitfalls
- Environmental damage
- Interactive elements
- Experimental hazards:
  - Frozen Ground: Slippery movement
  - Fire: Continuous damage
  - Poison Cloud: DoT effects
  - Electricity: Stun effects
  - Acid: Armor reduction

### Cover System
- Destructible objects
- Line of sight mechanics
- Position bonuses
- Experimental cover effects:
  - Zero Gravity: Floating cover
  - Frenzy: Ignore cover
  - Confusion: Random cover
  - Focus: Enhanced cover
  - Obsession: Target-based cover

### Line of Sight
- Visibility rules
- Stealth mechanics
- Detection system
- Experimental sight effects:
  - Blindness: No vision
  - Tunnel Vision: Limited view
  - Night Vision: Enhanced sight
  - Light Sensitivity: Bright light penalty
  - Obsession: Target tracking

## Combat Progression

### Character Growth
- Experience gain
- Skill development
- Ability unlocks
- Experimental progression:
  - Random skill boosts
  - Unexpected abilities
  - Chaotic learning
  - Focused training
  - Obsessive mastery

### Combat Challenges
- Daily missions
- Special events
- Boss encounters
- Experimental challenges:
  - Random modifiers
  - Chaotic conditions
  - Focused objectives
  - Obsessive goals
  - Co-op specific tasks

### Rewards & Loot
- Item drops
- Resource gathering
- Experience gain
- Experimental rewards:
  - Random effects
  - Chaotic items
  - Focused bonuses
  - Obsessive collections
  - Co-op specific loot

## Co-op Combat

### Team Coordination
- Role assignment
- Target focus
- Resource sharing
- Experimental teamwork:
  - Shared effects
  - Chaotic combos
  - Focused strategies
  - Obsessive coordination
  - Competitive elements

### Experimental Collaboration
- Shared discoveries
- Effect combinations
- Strategy development
- Co-op specific effects:
  - Team buffs/debuffs
  - Shared transformations
  - Coordinated chaos
  - Focused teamwork
  - Obsessive competition

### Social Dynamics
- Role-playing elements
- Competitive challenges
- Collaborative goals
- Experimental interactions:
  - Pranks and tricks
  - Chaotic fun
  - Focused competition
  - Obsessive rivalry
  - Team bonding

## Implementation Notes

### Technical Requirements
- Combat system architecture
- AI behavior trees
- Physics and collision
- Effect management system
- Co-op networking
- Experimental system integration

### UI Considerations
- Health and resource bars
- Ability cooldowns
- Status effect icons
- Experimental indicators:
  - Clear effect visuals
  - Simple feedback
  - Intuitive controls
  - Co-op information
  - Effect management

### Balance Considerations
- Damage calculations
- Resource costs
- Cooldown timers
- Experimental balance:
  - Fun vs. challenge
  - Co-op fairness
  - Effect potency
  - Duration balance
  - Interaction rules 