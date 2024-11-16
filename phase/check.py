from time import sleep

import enemy_data
import game_constants
import hero_data
import phase.phase_constants as phase_constants
from utility import print_abilities_points, print_items
from hero_data import available_points, fight_level
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

def battle_check(fight_leve, max_health):
    enemy_name= enemy_data.enemies[fight_leve]["name"]
    fight_against_text=""
    if fight_against_text==game_constants.BOSS_FIGHT_LEVEL:
        fight_against_text="Posledný súboj."+ enemy_name
    else:
        fight_against_text=enemy_name
    while True:
        print("0 - Odýchnuť si -" + rest_text(max_health))
        print("1 - Bojovať proti -"+ fight_against_text)
        print("2 - Upravit hrdinu")
        print("3 - Uložiť hru")
        print("4 - Ukončiť hru")

        choice = input("Čo chceš urobiť?")
        if choice not in ["0", "1","2", "3","4"]:
            print("Netrafil si ani jednú možnú voľbu. Musím sa ťa spýtať ešte raz")
            continue
        elif choice == "0":
            if hero_data.abilities["Život"]["points"]:
                print("Dobrá voľba, odýchni si")
                sleep(2)
                hero_data.abilities["Život"]["points"]= min(hero_data.abilities["Život"]["points"]+20, max_health)
                print(f"Tvoj život je na tom teraz takto: {str(hero_data.abilities['Život']['points'])} / {max_health}")
                print()
            else:
                print("Už máš plný život")
        elif choice == "1":
            return phase_constants.FIGHT
        elif choice =="2":
            hero_check()
        elif choice == "3":
            save_game(phase_constants.FIGHT, fight_level)
        elif choice == "4":
            if end_game_choice():
                return phase_constants.END
            else:
                print()
                continue


def rest_text(max_health):
    hero_current_life=hero_data.abilities["Život"]["points"]
    if hero_current_life<max_health:
        text=f"Obnoviť 20 života. Do plného ti chýba {str(max_health-hero_current_life)} bodov"
    else:
        text= "Máš síce plný život, ale odych nie je nikdy zlá voľba"
    return text

def hero_check():
    print(f"{hero_data.hero_name} tvoje schopnosti vyzerajú takto")
    print_abilities_points()

    if len(hero_data.hero_items)>0:
        print("Máš nasledujúce predmety (body sú už započítané v schopnostiach):")
        print_items()
    else:
        print("Nemáš žiadne predmety")
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
            continue






def phase_check(next_phase):
    if next_phase==phase_constants.FIGHT:
        continue_text = f"Súboj - LEVEL {str(hero_data.fight_level)}"
        if hero_data.fight_level == game_constants.BOSS_FIGHT_LEVEL:
            continue_text = f"Posledný {continue_text}"
    else:
        continue_text=next_phase

    while True:
        print("0 - Pokračovať na", continue_text)
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
            save_game(next_phase, fight_level)

        elif choice =="3":
            if end_game_choice():
                return phase_constants.END
            else:
                print()
                continue









