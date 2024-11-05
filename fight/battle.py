from enemy_data import enemies
import time
from hero_data import abilities
import game_constants

def calculate_hero_attack():
    base_attack = abilities["Útočná sila"]["points"]
    total_attack = (abilities["Útočná sila"]["points"] +
                    abilities["Obratnosť"]["points"] +
                    abilities["Skill"]["points"])

    return base_attack, total_attack

def calculate_enemy_attack(enemy_data):
    base_attack = enemy_data["Útočná sila"]
    total_attack = (enemy_data["Útočná sila"] +
                    enemy_data["Obratnosť"] +
                    enemy_data["Skill"])

    return base_attack, total_attack


def print_hero_stats(hero):
    print("Tvoj hrdina ide do súboja pripravený nasledovne:")
    print(f"Útok:minimum - {str(hero['attack'][0])}, maximum - {str(hero['attack'][1])}  ")
    print(f"Šanca na kritický útok - {str(hero['critital_hit'])} %")
    print(f"Obrana: minimum - {str(hero['defence'][0])}, maximum - {str(hero['defence'][1])}")
    print(f"život - {str(hero['health'])}")

def print_enemy_stats(enemy):
    print(f"Oproti nemu stojí príšera {enemy['name']} s nasledovnými schopnosťami ")
    print(f"Útok:minimum - {str(enemy['attack'][0])}, maximum - {str(enemy['attack'][1])}  ")
    print(f"Šanca na kritický útok - {str(enemy['critital_hit'])} %")
    print(f"Obrana: minimum - {str(enemy['defence'][0])}, maximum - {str(enemy['defence'][1])}")
    print(f"život - {str(enemy['health'])}")

def simulate_battle(hero, enemy):
    print_hero_stats(hero)
    print()
    time.sleep(1)
    print_enemy_stats(enemy)
    time.sleep(3)
    print(game_constants.DIVIDER)
    print("\nZačíname súboj ako prvý útočiš ty.\n")


def battle(fight_level):
    print("Tvoj hrdina ide do súboja nasledovne:")
    enemy_data=enemies[fight_level]

    hero={
        "critital_hit": min(100,(abilities["Skill"]["points"] * abilities["Šťastie"]["points"])//2),
        "defence": (abilities["Obrana"]["points"], abilities      ["Obrana"]["points"]+abilities["Obratnosť"]["points"]),
        "attack": calculate_hero_attack(),
        "health":abilities["Život"]["points"]
    }

    enemy={
       "name": enemy_data["name"],
        "attack":calculate_enemy_attack(enemy_data),
        "critital_hit":min(100,(enemy_data["Skill"] * enemy_data["Šťastie"])//2),
        "defence": (enemy_data["Obrana"],
                   enemy_data["Obrana"] + enemy_data["Obratnosť"]),
        "health": enemy_data["Život"]
   }

    simulate_battle(hero, enemy)
