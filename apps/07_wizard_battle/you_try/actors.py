import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return f"{self.name} level {self.level}"

    def roll(self):
        roll = random.randint(0,self.level)
        return roll


class Wizard(Creature):
    def __init__(self, name, level=10):
        super().__init__(name, level=10)

    def level_up(self, increase):
        self.level += increase
        print(f"You increased your level by {increase}. {self.name}'s level is now {self.level}")

    def attack(self, enemy):
        enemy_roll = enemy.roll()
        my_roll = self.roll()
        print(f"You've rolled {my_roll}")
        print(f"Enemy rolled {enemy_roll}")

        if my_roll >= enemy_roll:
            print(f"Wizard {self.name} won, {enemy.name} has been defeated!")
            self.level_up(enemy.level)
            result = "win"
        else:
            print(f"Wizard {self.name} lost! Game over")
            result = "lost"

        return result


class SmallAnimal(Creature):
    level_limit = 20

    def __init__(self, name, level):
        super().__init__(name, level)

    def roll(self):
        base_roll = super().roll()
        return int(round((base_roll / 2),0))


class Dragon(Creature):

    def __init__(self, name, level, elemental_type):
        super().__init__(name, level)
        self.elemental_type = elemental_type

    def roll(self):
        roll = super().roll()
        final_roll = roll

        if self.elemental_type == "ice":
            final_roll = roll * 1.2
        elif self.elemental_type == "fire":
            final_roll = roll * 1.6
        elif self.elemental_type == "dark":
            final_roll = roll * 1.9

        return final_roll
