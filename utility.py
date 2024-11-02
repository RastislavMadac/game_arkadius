from hero_data import abilities
from game_constants import DIVIDER

def print_abilities_description():
  print(DIVIDER)
  for k,v in abilities.items():
      print(f"{k} - {v['description']}")
  print(DIVIDER)

def print_abilities_options(with_help_option=False):
    if with_help_option:
            print("0 - Vysvetlivky - načo sú dobré jednoltlivé schopnosti")

    for i, ability in enumerate(abilities.keys()):
        ability_option = str(i + 1) + ' - ' + ability
        if ability == "Život":
            ability_option += " " + "- jeden bod pridá 5 života"
        print(ability_option)

def print_abilities_points():
    for k, v in abilities.items():
        print(k + " - " + str(v["points"]), end=", ")
    print("\n")

