import random
import time

MASSIVE_EXPLOSION = """
   ╱▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀╲
  ▕    🔥 MASSIVE EXPLOSION 🔥   ▏
   ╲▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄╱
           ▄▄▄▄▄▄▄▄
      ▄▄██████████████▄▄
   ▄██████████████████████▄
  ███████████████████████████
  ███████████████████████████
  ███████████████████████████
   ▀█████████████████████▀
      ▀█████████████▀▀
"""

ALIEN_VICTORY = """
    🛸 EARTH CONQUERED 🌍
         ▄▄▄▄▄▄▄▄▄
    ▄▀█████████████████▀▄
    █████████████████████
    ▀█████████████████▀
        ▀█████████▀
"""

HUMAN_VICTORY = """
    🌟 HUMANITY TRIUMPHS 🌟
      ♦  ♦  ♦  ♦  ♦
    👮‍♂️ 🎖️ 💪 🇺🇸 🏆
    DEFENDERS OF EARTH
    STAND VICTORIOUS!
"""

ALIEN_ART = """
    👽 ALIEN ARRIVAL 👽
       ▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄
    ████▒▒░░░░░░▒▒████
    ████░░░░░░░░░░████
    ████░░█░░░░█░░████
    ████░░░░▀▀░░░░████
    ████░░░░░░░░░░████
     ███░░░░░░░░░░███
       ▀▀▀▀▀▀▀▀▀▀▀
"""

class AlienInvasionGame:
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_health = 100
        self.city_health = 100
        self.alien_fleet_size = 10
        self.score = 0
        self.attack_sequence = []
        self.is_alien_mode = False
        
        # Predefined alien names
        self.alien_names = [
            "Zorg the Conqueror", 
            "Klaatu Verada", 
            "Supreme Commander Xax", 
            "Lord Nebula", 
            "Emperor Zylax"
        ]
        self.alien_commander_name = ""
        
        self.human_weapons = {
            "laser": {"damage": 20, "accuracy": 0.7, "crit_chance": 0.2},
            "missile": {"damage": 35, "accuracy": 0.5, "crit_chance": 0.3},
            "emp": {"damage": 15, "accuracy": 0.6, "crit_chance": 0.1}
        }
        
        self.alien_weapons = {
            "plasma_cannon": {"damage": 30, "accuracy": 0.8, "crit_chance": 0.25},
            "mind_control": {"damage": 25, "accuracy": 0.6, "crit_chance": 0.15},
            "quantum_disruptor": {"damage": 40, "accuracy": 0.4, "crit_chance": 0.35}
        }

    def display_status(self):
        print("\n--- INVASION STATUS ---")
        print(f"{'Player' if not self.is_alien_mode else 'Alien'} Health: {self.player_health}")
        print(f"{'City' if not self.is_alien_mode else 'Human Resistance'} Health: {self.city_health}")
        print(f"{'Alien' if not self.is_alien_mode else 'Human'} Fleet Remaining: {self.alien_fleet_size}")
        print(f"Current Score: {self.score}")

    def choose_weapon(self):
        weapons = self.alien_weapons if self.is_alien_mode else self.human_weapons
        
        print("\nChoose your weapon:")
        for weapon, stats in weapons.items():
            print(f"{weapon.capitalize()}: Damage {stats['damage']}, Accuracy {stats['accuracy']*100}%")
        
        while True:
            choice = input(f"Select weapon ({'/'.join(weapons.keys())}) or special command: ").lower()
            
            # Secret mode trigger
            if not self.is_alien_mode and choice == "emp":
                self.attack_sequence.append("emp")
            elif not self.is_alien_mode and choice == "missile" and self.attack_sequence == ["emp"]:
                self.attack_sequence.append("missile")
            
            if choice in weapons:
                return choice
            
            # Easter egg trigger
            if choice == "all your base belong to us" and len(self.attack_sequence) == 2:
                print("\n🛸 TRANSFORMATION COMPLETE: YOU ARE NOW THE ALIEN! 👽")
                print(ALIEN_ART)
                self.is_alien_mode = True
                self.player_health = 150  # Bonus health for alien mode
                self.alien_fleet_size = 5  # Reduced fleet size
                
                # Select a random alien commander name
                self.alien_commander_name = random.choice(self.alien_names)
                print(f"Greetings, newest recruit! I am {self.alien_commander_name}, Supreme Leader of the Invasion Fleet!")
                
                return list(self.alien_weapons.keys())[0]
            
            print("Invalid weapon. Try again.")

    def alien_attack(self):
        damage = random.randint(10, 25)
        defense_roll = random.random()
        
        if defense_roll < 0.4:  # 40% chance to partially defend
            damage //= 2
        
        self.player_health -= damage
        self.city_health -= damage // 2
        attacker = "Alien" if not self.is_alien_mode else "Human"
        print(f"\n🛸 {attacker} attack! You took {damage} damage. {'City' if not self.is_alien_mode else 'Alien Base'} took {damage//2} damage.")

    def player_attack(self, weapon):
        weapons = self.alien_weapons if self.is_alien_mode else self.human_weapons
        weapon_stats = weapons[weapon]
        accuracy_roll = random.random()
        crit_roll = random.random()
        
        if accuracy_roll < weapon_stats['accuracy']:
            damage = weapon_stats['damage']
            
            # Critical hit check
            if crit_roll < weapon_stats['crit_chance']:
                damage *= 2
                print("\n💥 CRITICAL HIT! MASSIVE DAMAGE!")
                print(MASSIVE_EXPLOSION)
            
            self.alien_fleet_size -= 1
            self.score += 50
            attacker = "Player" if not self.is_alien_mode else "Alien"
            print(f"\n💥 Direct hit! {attacker}'s {weapon.capitalize()} destroyed an enemy ship. +50 points!")
        else:
            attacker = "Player" if not self.is_alien_mode else "Alien"
            print(f"\n❌ {attacker}'s {weapon.capitalize()} missed the enemy ship!")

    def game_over_check(self):
        if self.player_health <= 0:
            print(f"\n☠️ GAME OVER: {'You' if not self.is_alien_mode else 'Humans'} were defeated!")
            if self.is_alien_mode:
                print(HUMAN_VICTORY)
            else:
                print(ALIEN_VICTORY)
            return True
        if self.city_health <= 0:
            print(f"\n🏙️ GAME OVER: {'Your city' if not self.is_alien_mode else 'Human Resistance'} has been destroyed!")
            if self.is_alien_mode:
                print(HUMAN_VICTORY)
            else:
                print(ALIEN_VICTORY)
            return True
        if self.alien_fleet_size <= 0:
            message = "🎉 VICTORY: " + ("You've repelled the alien invasion!" if not self.is_alien_mode else "Aliens have conquered Earth!")
            print(f"\n{message}")
            if not self.is_alien_mode:
                print(HUMAN_VICTORY)
            else:
                print(ALIEN_VICTORY)
            return True
        return False

    def play(self):
        print(f"🛸 WELCOME, {self.player_name}! 🌍")
        print("Defend Earth from the alien armada!")
        
        while True:
            self.display_status()
            
            weapon = self.choose_weapon()
            self.player_attack(weapon)
            
            if random.random() < 0.8:  # 80% chance of enemy counterattack
                self.alien_attack()
            
            if self.game_over_check():
                print(f"\nFinal Score: {self.score}")
                break
            
            time.sleep(1)

def main():
    print("🌍 ALIEN INVASION DEFENSE SIMULATOR 🛸")
    player_name = input("Enter your name, brave soldier: ")
    game = AlienInvasionGame(player_name)
    game.play()

if __name__ == "__main__":
    main()
