import random
import time

class Character:
    def __init__(self, name, sanity, strength, knowledge, willpower):
        self.name = name
        self.sanity = sanity
        self.strength = strength
        self.knowledge = knowledge
        self.willpower = willpower
        self.max_sanity = sanity
        self.max_health = 100
        self.inventory = []

    def take_damage(self, damage):
        self.sanity -= damage
        return self.sanity <= 0

    def heal_sanity(self, amount):
        healed = min(amount, self.max_sanity - self.sanity)
        self.sanity = min(self.sanity + amount, self.max_sanity)
        return f"Healed {healed} sanity points."

    def is_defeated(self):
        return self.sanity <= 0

    def add_to_inventory(self, item):
        self.inventory.append(item)

class Player(Character):
    def __init__(self, name, sanity, strength, knowledge, willpower):
        super().__init__(name, sanity, strength, knowledge, willpower)
        self.item_found = False
        self.lives = 2

class Enemy(Character):
    def __init__(self, name, sanity, strength, knowledge, willpower, terror_level):
        super().__init__(name, sanity, strength, knowledge, willpower)
        self.terror_level = terror_level

class CosmicHorror(Character):
    def __init__(self, name, sanity, strength, knowledge, willpower, horror_type):
        super().__init__(name, sanity, strength, knowledge, willpower)
        self.horror_type = horror_type

    def special_attack(self, target):
        damage_multipliers = {
            "Dimensional Writhing": 1.5,
            "Void Consumption": 1.7,
            "Quantum Fragmentation": 2.0,
            "Temporal Corruption": 2.2
        }
        
        base_damage = random.randint(20, 40)
        multiplier = damage_multipliers.get(self.horror_type, 1.5)
        damage = int(base_damage * multiplier)
        
        target.take_damage(damage)
        print(f"{self.name} unleashes a devastating {self.horror_type} attack!")
        print(f"Deals {damage} damage to {target.name}!")

# Enemy Descriptions
ENEMY_DESCRIPTIONS = {
    "Whispering Shadow": """
    A writhing darkness coalesces, edges blurred and indistinct.
    Whispers crawl across your skin, promising unspeakable terrors.
    Tendrils of absolute void reach out, hungry and formless.
    """,
    
    "Tentacled Abomination": """
    Impossible geometries twist and pulse with alien rhythms.
    Wet, membranous appendages unfurl from impossible angles.
    Each tentacle seems to exist in multiple dimensions simultaneously.
    """,
    
    "Dimensional Breach Entity": """
    Reality fractures around its impossible form.
    Spaces between spaces leak malevolent consciousness.
    Fragments of nightmares congeal into a sentient horror.
    """
}

class EnemyTransition:
    def __init__(self, name, description=None):
        self.name = name
        self.description = description or ENEMY_DESCRIPTIONS.get(name, "A terrifying entity approaches...")

    def display_transition(self, delay_multiplier=1):
        print(f"\n--- APPROACHING: {self.name.upper()} ---")
        for line in self.description.strip().split('\n'):
            for char in line:
                print(char, end='', flush=True)
                time.sleep(0.03 * delay_multiplier)
            print()
            time.sleep(0.5 * delay_multiplier)
        print()
        time.sleep(1 * delay_multiplier)

def create_custom_character():
    print("\nCreate Your Character")
    name = input("Enter your character's name: ")
    
    # Special Easter Egg for Allyne Roil
    if name.lower() == "allyne roil":
        print("\n*** COSMIC HORROR TRANSFORMATION INITIATED ***")
        return select_cosmic_horror()
    
    print("\nDistribute 20 points across Sanity, Strength, Knowledge, and Willpower")
    
    stats = {'Sanity': 0, 'Strength': 0, 'Knowledge': 0, 'Willpower': 0}
    total_points = 20
    
    for stat in stats.keys():
        while True:
            try:
                points = int(input(f"Points for {stat} (Remaining: {total_points}): "))
                if 0 <= points <= total_points:
                    stats[stat] = points
                    total_points -= points
                    break
                else:
                    print(f"Invalid input. Must be between 0 and {total_points}.")
            except ValueError:
                print("Please enter a valid number.")
    
    return Player(name, stats['Sanity'], stats['Strength'], 
                  stats['Knowledge'], stats['Willpower'])

def predefined_characters():
    characters = [
        Player("Dr. Eliza Blackwood", 25, 10, 20, 15),
        Player("Jack Harrow", 20, 18, 10, 10),
        Player("Miranda Chen", 25, 8, 15, 19)
    ]
    return characters

def create_cosmic_horror_options():
    return [
        CosmicHorror("Dimensional Writhing Entity", 100, 25, 30, 40, "Dimensional Writhing"),
        CosmicHorror("Void Consuming Abomination", 120, 35, 20, 35, "Void Consumption"),
        CosmicHorror("Quantum Fragmenting Nightmare", 90, 30, 40, 45, "Quantum Fragmentation"),
        CosmicHorror("Temporal Corrupting Anomaly", 110, 20, 45, 50, "Temporal Corruption")
    ]

def select_cosmic_horror():
    horrors = create_cosmic_horror_options()
    print("\n=== COSMIC HORROR TRANSFORMATION ===")
    
    # Transformation narrative
    transformation_stages = [
        "Your body begins to feel... different.",
        "Strange sensations ripple through your consciousness.",
        "Reality warps around you as your humanity slips away...",
        "TRANSFORMATION COMPLETE"
    ]
    
    for stage in transformation_stages:
        for char in stage:
            print(char, end='', flush=True)
            time.sleep(0.1)
        print()
        time.sleep(0.5)
    
    for i, horror in enumerate(horrors, 1):
        print(f"{i}. {horror.name} ({horror.horror_type})")
    
    while True:
        try:
            choice = int(input("Select your horror form (1-4): "))
            if 1 <= choice <= 4:
                return horrors[choice - 1]
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")

def get_random_item():
    items = [
        {"name": "knife", "damage": 15, "probability": 0.4},
        {"name": "gun", "damage": 25, "probability": 0.25},
        {"name": "bomb", "damage": 35, "probability": 0.15},
        {"name": "wand", "damage": 45, "probability": 0.1},
        {"name": "staff", "damage": 60, "probability": 0.05}
    ]
    
    random_value = random.random()
    cumulative_prob = 0
    
    for item in items:
        cumulative_prob += item["probability"]
        if random_value <= cumulative_prob:
            return item
    
    return items[0]  # Default to knife if something goes wrong

def create_enemies():
    return [
        Enemy("Whispering Shadow", 30, 15, 10, 20, 8),
        Enemy("Tentacled Abomination", 40, 20, 15, 25, 10),
        Enemy("Dimensional Breach Entity", 50, 25, 30, 30, 12)
    ]

def combat_encounter(player, enemies):
    print(f"\n--- ENCOUNTER ---")
    
    if isinstance(player, CosmicHorror):
        # Full combat for Cosmic Horror against human enemies
        while not player.is_defeated() and any(not enemy.is_defeated() for enemy in enemies):
            print(f"\n{player.name}'s Sanity: {player.sanity}")
            
            # Choose a living enemy target
            living_enemies = [enemy for enemy in enemies if not enemy.is_defeated()]
            target = random.choice(living_enemies)
            
            # Cosmic Horror's special attack
            player.special_attack(target)
            
            # Counterattack from living enemies
            for enemy in living_enemies:
                if not player.is_defeated():
                    enemy_damage = random.randint(1, max(5, enemy.strength // 2))
                    player.take_damage(enemy_damage)
                    print(f"{enemy.name} counterattacks, dealing {enemy_damage} damage!")
            
            print(f"{player.name}'s current Sanity: {player.sanity}")
            print(f"{target.name}'s current Sanity: {target.sanity}")
        
        return not player.is_defeated()
    
    for enemy in enemies:
        while not player.is_defeated() and not enemy.is_defeated():
            print(f"\n{player.name}'s Sanity: {player.sanity}")
            print(f"{enemy.name}'s Sanity: {enemy.sanity}")
            
            # Display inventory if items exist
            if player.inventory:
                print("Inventory:", ", ".join(item['name'] for item in player.inventory))
            
            # Potential item discovery
            if not player.item_found and random.random() < 0.3:
                item = get_random_item()
                print(f"You discovered a {item['name']}!")
                player.add_to_inventory(item)
                player.item_found = True
            
            action = input("Choose action (1: Attack, 2: Defend, 3: Special Item, 4: Heal): ")
            
            if action == '1':  # Normal Attack
                player_damage = random.randint(5, player.strength)
                enemy_damage = random.randint(1, max(5, enemy.strength // 2))
                
                enemy.take_damage(player_damage)
                player.take_damage(enemy_damage)
                
                print(f"You deal {player_damage} damage to {enemy.name}!")
                print(f"{enemy.name} deals {enemy_damage} damage to you!")
            
            elif action == '2':  # Defend
                player_defense = random.randint(1, player.willpower)
                enemy_damage = max(0, random.randint(5, enemy.strength) - player_defense)
                
                player.take_damage(enemy_damage)
                print(f"You defend, reducing damage to {enemy_damage}!")
            
            elif action == '3' and player.inventory:  # Special Item
                item = player.inventory[0]
                player.inventory.pop(0)
                print(f"You use the {item['name']} for a devastating attack!")
                enemy.take_damage(item['damage'])
                print(f"Deals {item['damage']} damage to {enemy.name}!")
            
            elif action == '4':  # Heal
                heal_amount = random.randint(5, player.willpower)
                result = player.heal_sanity(heal_amount)
                print(result)
    
            # Check for player defeat with lives system
            if player.is_defeated():
                if player.lives > 0:
                    player.lives -= 1
                    player.sanity = player.max_sanity // 2
                    print(f"You were overwhelmed, but manage to recover! {player.lives} lives remaining.")
                else:
                    print("Your sanity has been overwhelmed. The cosmic horror consumes you...")
                    return False
    
    return True

def main_game():
    print("=== COSMIC HORROR ADVENTURE ===")
    print("Choose your character:")
    
    characters = predefined_characters()
    for i, char in enumerate(characters, 1):
        print(f"{i}. {char.name}")
    print("4. Create Custom Character")
    
    while True:
        try:
            choice = int(input("Select character (1-4): "))
            if 1 <= choice <= 3:
                player = characters[choice - 1]
            elif choice == 4:
                player = create_custom_character()
            else:
                print("Invalid choice. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a number.")
    
    # Modify enemy creation to support Cosmic Horror scenario
    if isinstance(player, CosmicHorror):
        enemies = predefined_characters()
    else:
        enemies = create_enemies()
    
    # Track defeated enemies to ensure proper transitions
    for i, enemy in enumerate(enemies):
        # Create enemy transition
        transition = EnemyTransition(enemy.name)
        
        # If it's not the first enemy, announce previous enemy's defeat
        if i > 0:
            print(f"\n=== {enemies[i-1].name} has been defeated! ===")
        
        # Display transition for current enemy
        transition.display_transition()
        
        if not combat_encounter(player, [enemy]):
            print("GAME OVER")
            return
    
    print("Congratulations! You survived the cosmic horror... for now.")

if __name__ == "__main__":
    main_game()
