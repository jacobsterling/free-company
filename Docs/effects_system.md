# Effects System

## Overview

The effects system in Free Company is a comprehensive framework that tracks and manages all active effects on characters, both players and enemies. Effects can be physical, mental, environmental, or magical in nature, and can interact with each other in complex ways. The system is designed to create meaningful gameplay choices and consequences for player actions.

## Effect Categories

### Physical Effects
1. **Bleeding**
   - Damage over time
   - Reduced healing effectiveness
   - Can be stopped with bandages
   - Stacks with multiple sources

2. **Poisoned**
   - Damage over time
   - Reduced stamina regeneration
   - Can be cured with antidotes
   - Different poison types have different effects

3. **Burned**
   - Damage over time
   - Reduced armor effectiveness
   - Can be extinguished with water
   - Fire spreads to nearby flammable objects

4. **Frozen**
   - Reduced movement speed
   - Increased vulnerability to physical damage
   - Can be thawed with heat sources
   - Shatters when hit with physical damage

5. **Blindness**
   - Reduced vision range
   - Increased chance to miss attacks
   - Can be cured with eye drops
   - Temporary or permanent

6. **Deafness**
   - Cannot hear sound cues
   - Affects voice chat functionality
   - Can be cured with ear drops
   - Temporary or permanent

7. **Crippled**
   - Reduced movement speed
   - Cannot sprint
   - Can be treated with splints
   - Requires rest to heal

8. **Vampirism**
   - Enhanced night vision
   - Regeneration in darkness
   - Damage in sunlight
   - Blood hunger replaces food requirements
   - Increased stress resistance in darkness
   - Increased stress in sunlight
   - Can transform into bat form
   - Transmitted through blood contact
   - Curable with specific items
   - Permanent if not treated quickly

### Mental Effects
1. **Stress**
   - Increases over time in dangerous situations
   - Reduced by rest and relaxation
   - Can lead to mental breakdowns
   - Affects decision making

2. **Paranoia**
   - Increased perception of threats
   - May attack allies
   - Reduced trust in others
   - Can be treated with calming herbs

3. **Frenzy**
   - Increased damage
   - Reduced defense
   - Cannot use complex abilities
   - Temporary or until condition is met

4. **Confusion**
   - Random movement
   - May use wrong abilities
   - Disoriented navigation
   - Can be cured with clarity potions

5. **Possession**
   - Loss of control
   - Controlled by another entity
   - Special abilities while possessed
   - Can be exorcised with holy items

6. **Bloodlust**
   - Increased damage
   - Must attack to satisfy
   - Reduced control
   - Specific to vampire characters

### Environmental Effects
1. **Wet**
   - Increased vulnerability to lightning
   - Reduced vulnerability to fire
   - Slower movement on certain surfaces
   - Can be dried with heat

2. **Covered in Blood**
   - Attracts predators
   - Increased stealth in dark areas
   - Can be washed off with water
   - May cause fear in certain enemies

3. **On Fire**
   - Damage over time
   - Spreads to nearby flammable objects
   - Can be extinguished with water
   - Increased vulnerability to fire damage

4. **In Darkness**
   - Increased stress
   - Reduced vision
   - Enhanced stealth
   - Beneficial for vampires

5. **In Sunlight**
   - Reduced stress
   - Enhanced vision
   - Reduced stealth
   - Damaging for vampires

### Magical Effects
1. **Blessed**
   - Increased resistance to negative effects
   - Enhanced healing
   - Glowing aura
   - Temporary or permanent

2. **Cursed**
   - Increased vulnerability to negative effects
   - Reduced healing
   - Dark aura
   - Temporary or permanent

3. **Enchanted**
   - Enhanced weapon damage
   - Special weapon effects
   - Glowing weapon
   - Temporary or permanent

4. **Polymorphed**
   - Transformed into another creature
   - New abilities based on form
   - Temporary or until condition is met
   - Can be dispelled with specific items

5. **Invisible**
   - Cannot be seen by enemies
   - Reduced noise
   - Cannot interact with most objects
   - Temporary or until condition is met

## Effect Interactions

### Effect Stacking
- Multiple effects of the same type can stack
- Stacking limits based on effect type
- Some effects cancel each other out
- Some effects enhance each other

### Effect Combinations
1. **Bleeding + Poisoned**
   - Increased damage over time
   - Poison enters bloodstream faster

2. **Frozen + Physical Damage**
   - Shatters frozen target
   - Area damage to nearby enemies

3. **On Fire + Wet**
   - Creates steam cloud
   - Reduced visibility

4. **Vampirism + In Darkness**
   - Enhanced regeneration
   - Increased strength

5. **Vampirism + In Sunlight**
   - Severe damage over time
   - Reduced abilities

### Effect Triggers
- Time-based triggers
- Condition-based triggers
- Interaction-based triggers
- Environment-based triggers

## Effect Management

### Application
- Direct application from abilities
- Environmental exposure
- Item consumption
- Enemy attacks
- Trap triggers

### Removal
- Time expiration
- Condition fulfillment
- Item consumption
- Ability usage
- Environmental interaction

### Resistance
- Character-based resistance
- Equipment-based resistance
- Temporary resistance buffs
- Immunity to specific effects

### UI Representation
- Visual indicators
- Status icons
- Effect timers
- Stack counters
- Color coding

## Implementation Notes

### Technical Requirements
- Effect tracking system
- Effect interaction logic
- UI for effect display
- Effect application and removal
- Resistance calculation

### UI Considerations
- Clear visual indicators
- Effect duration display
- Stack count for multiple effects
- Effect source information
- Removal instructions

### Balance Considerations
- Effect duration
- Effect potency
- Application frequency
- Removal difficulty
- Resistance availability
- Effect combinations
- Vampirism progression and balance 