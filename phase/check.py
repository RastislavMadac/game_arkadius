
import hero_data
import phase.phase_constants as phase_constants
from utility import print_abilities_points
from hero_data import available_points
from hero_update import hero_update
from save_load import save_game


def end_game_choice():
    print("Si si isty, že chceš ukončiť hru?")

    while True:
        print("0 - Späť")
        print("1 - Áno, ukončiť.")
        choice = input("Naozaj ukonciť? ")
        if choice not in ["0", "1"]:
            print("Netrafil si, pýtam sa ešte raz")
            continue
        if choice == "0":
            return False
        elif choice == "1":
            return True

def hero_check():
    print(f"{hero_data.hero_name} tvoje schopnosti vyzerajú takto")
    print_abilities_points()
    print(f"Máš {available_points} bodov na pridávanie schopností")

    while True:
        print("0 - Späť")
        print("1 - Upraviť schopnosti hrdiny")

        choice=input("Čo chceš urobiť?")

        if choice not in ["0", "1"]:
            print("Netrafil si ani jednú možnú voľbu. Musím sa ťa spýtať ešte raz")
            continue
        elif choice=="0":
            break
        elif choice == "1":
            hero_update()





def phase_check(next_phase):
    while True:
        print("0 - Pokračovať na", next_phase)
        print("1 - Upraviť hrdinu")
        print("2 - Uložiť hru")
        print("3 - Ukončiť hru")

        choice=input("Aký je tvoj další krok?")
        #choice = "1"
        if choice not in ["0", "1", "2", "3"]:
            print("Netrafil si ani jednú možnú voľbu. Musím sa ťa spýtať ešte raz")
            continue

        if choice =="0":

           return next_phase
        elif choice =="1":
            hero_check()
            continue
        elif choice =="2":
            save_game(next_phase)

        elif choice =="3":
            if end_game_choice():
                return phase_constants.END
            else:
                print()
                continue









