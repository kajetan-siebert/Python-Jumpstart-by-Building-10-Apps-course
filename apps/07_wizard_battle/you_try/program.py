import random

import actors


def main():
    print_header()
    hero = create_hero()
    enemies = create_enemies()

    result = ""
    enemy = random_encounter(enemies)

    while result != "lost":
        action = hero_action()

        if action == "a":
            result = hero.attack(enemy)
            if result != "lost":
                enemies.remove(enemy)
                enemy = random_encounter(enemies)

        elif action == "r":
            print(f"You've run away from {enemy}")
            enemy = random_encounter(enemies)

        elif action == "l":
            print("You see your enemies:")
            for enemy in enemies:
                print(enemy)







def print_header():
    print("------------------------------------")
    print("---------Wizard Battle app----------")
    print("------------------------------------")


def create_enemies():
    number_of_enemies = int(input("Enter the number of enemies: "))
    enemy_list = []
    for i in range(number_of_enemies):
        enemy = generate_enemy()
        enemy_list.append(enemy)

    return enemy_list


def generate_enemy():
    animal_names = ["Infected Goose", "Angry Boar", "Snake", "Wolf",
                    "Dark Rat"]
    dragon_names = ["Viserion Dragon", "Drogo Dragon", "Finaenedal Dragon",
                    "Berys"]
    animal_level_range = (1, 20)
    dragon_level_range = (20, 100)
    elemental_types = ["fire", "ice", "dark" "normal"]

    enemy_type = random.choice(["Dragon", "Small Animal"])

    if enemy_type == "Dragon":
        name = random.choice(dragon_names)
        level = random.randint(dragon_level_range[0], dragon_level_range[1])
        elemental_type = random.choice(elemental_types)
        enemy = actors.Dragon(name, level, elemental_type)

    elif enemy_type == "Small Animal":
        name = random.choice(animal_names)
        level = random.randint(animal_level_range[0], animal_level_range[1])
        enemy = actors.SmallAnimal(name, level)

    else:
        enemy = None

    return enemy


def create_hero():
    hero_name = input(f"Enter your hero name: ")
    hero = actors.Wizard(hero_name)
    return hero


def hero_action():
    action_choice = ""
    while action_choice != "a" and action_choice != "r" and action_choice != "l":
        action_choice = input("What do you want to do? [A]ttack, [R]un away or [l]ook around?\n")
        if action_choice != "a" and action_choice != "r" and action_choice != "l":
            print("Command unrecognized, try again")
    return action_choice


def random_encounter(enemies_list):
    random_enemy = random.choice(enemies_list)
    print(f"You encountered {random_enemy}")
    return random_enemy


if __name__ == '__main__':
    main()
