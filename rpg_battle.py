import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def take_damage(self, damage):
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.take_damage(damage)
        return damage

    def special_move(self, other):
        damage = random.randint(1, self.attack_power)
        other.take_damage(damage)
        return damage


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)
        self.armour = 5

    def take_damage(self, damage):
        actual_damage = damage - self.armour
        if actual_damage < 0:
            actual_damage = 0
        self.health = self.health - actual_damage
        if self.health < 0:
            self.health = 0

    def special_move(self, other):
        damage = random.randint(15, 35)
        other.take_damage(damage)
        return damage


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=15)
        self.spells_left = 3

    def special_move(self, other):
        if self.spells_left == 0:
            print("No spells left!")
            return 0
        damage = self.attack_power * 2
        other.take_damage(damage)
        self.spells_left = self.spells_left - 1
        return damage


def save_result(player_name, enemy_name, winner):
    file = open("results.txt", "a")
    file.write(player_name + " vs " + enemy_name + " -- Winner: " + winner + "\n")
    file.close()


def battle(player, enemy):
    print("\n--- Battle Start: " + player.name + " vs " + enemy.name + " ---\n")

    while player.is_alive() and enemy.is_alive():
        print(player.name + " HP: " + str(player.health))
        print(enemy.name + " HP: " + str(enemy.health))
        print("")

        if isinstance(player, Mage):
            print("1. Attack  2. Cast Spell (" + str(player.spells_left) + " left)  3. Run")
        else:
            print("1. Attack  2. Special Move  3. Run")

        choice = input("Your choice: ")

        if choice == "1":
            damage = player.attack(enemy)
            print(player.name + " attacks for " + str(damage) + " damage!")
        elif choice == "2":
            damage = player.special_move(enemy)
            if damage > 0:
                print(player.name + " uses special move for " + str(damage) + " damage!")
        elif choice == "3":
            print(player.name + " ran away!")
            save_result(player.name, enemy.name, "Nobody (ran away)")
            return
        else:
            print("Invalid choice, you lose your turn!")

        if enemy.is_alive():
            damage = enemy.attack(player)
            print(enemy.name + " attacks back for " + str(damage) + " damage!")

        print("")

    if player.is_alive():
        print(player.name + " wins!")
        save_result(player.name, enemy.name, player.name)
    else:
        print(enemy.name + " wins!")
        save_result(player.name, enemy.name, enemy.name)


def main():
    print("Welcome to the RPG Battle Simulator!")
    print("")

    name = input("Enter your character name: ")

    print("Pick a class:")
    print("1. Warrior (high HP, armour)")
    print("2. Mage (low HP, powerful spells)")

    class_choice = input("Your choice: ")

    if class_choice == "1":
        player = Warrior(name)
    else:
        player = Mage(name)

    enemy_names = ["Goblin", "Orc", "Dark Knight", "Skeleton"]
    enemy_name = random.choice(enemy_names)
    enemy = Character(enemy_name, health=80, attack_power=15)

    battle(player, enemy)


main()
