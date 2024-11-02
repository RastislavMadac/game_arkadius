
import hero_data
from utility import  print_abilities_options, print_abilities_points

def hero_add_point():
    while True:
        if hero_data.available_points < 1:
            break
        print(f"Máš {hero_data.available_points} bodov na pridelenie schopností")

        print("0 - Už nechcem pridať body- (Späť)")
        print_abilities_options()
        option = input("Ktorej schopnosti chceš pridať bod?")

        if option =="0":
          break

        elif option.isnumeric() and int(option) in list(range(1, len(hero_data.abilities) + 1)):
            chosen_ability_name = list(hero_data.abilities.keys())[int(option) - 1]
            chosen_ability = hero_data.abilities[chosen_ability_name]

            print("\nVybral si si schopnosť - " + chosen_ability_name + ". Pridávam ti bod.")

            if chosen_ability_name == 'Život':
                chosen_ability["points"] += 5
            else:
                chosen_ability["points"] += 1

            hero_data.available_points -=1
            print("Teraz tvoje body vyzerajú takto: ")
            print_abilities_points()
        else:
            print("Netrafil si výber, musím sa ťa spýtať ešte raz. \n")
            continue


def hero_substract_point():
    while True:
        print(f"Máš {hero_data.available_points} bodov na pridelenie schopností")

        print("0 - Už nechcem odoberať body- (Späť)")
        print_abilities_options()
        option = input("Ktorej schopnosti chceš odobrať bod?")

        if option =="0":
          break

        elif option.isnumeric() and int(option) in list(range(1, len(hero_data.abilities) + 1)):
            chosen_ability_name = list(hero_data.abilities.keys())[int(option) - 1]
            chosen_ability = hero_data.abilities[chosen_ability_name]

            print("\nVybral si si schopnosť - " + chosen_ability_name + ". Odoberám ti bod.")

            if chosen_ability["points"] < 1:
                print("Dannej schopnosti nemôžeš odobrať bod")
                break


            if chosen_ability_name == 'Život':
                    chosen_ability["points"] -= 5
            else:
                    chosen_ability["points"] -= 1

            hero_data.available_points +=1

            print("Teraz tvoje body vyzerajú takto: ")
            print_abilities_points()
        else:
            print("Netrafil si výber, musím sa ťa spýtať ešte raz. \n")
            continue


def hero_update():
    while True:
        print("0 - Späť")
        print(f"1 - Pridať body (máš {hero_data.available_points} bodov na pridelenie schopností")
        print("2 - Odstránenie schopností")

        choice= input("Aká je tvoja voľba?")
        if choice not in ["0", "1", "2"]:
            print("Netrafil si ani jednú možnú voľbu. Musím sa ťa spýtať ešte raz")
            continue
        elif choice=="0":
            break
        elif choice == "1":
            hero_add_point()
            continue
        elif choice == "2":
            hero_substract_point()








