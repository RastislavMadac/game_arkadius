import hero_data
import phase.phase_constants as phase_constants
from phase.check import phase_check
from save_load import load_game


def start_phase():
    while True:
        print("0 - Začať novú hru \n"
              "1 - Načítať uloženú hru")
        start_choice=input("Aká je tvoja voľba?")
        if start_choice not in ["0", "1"]:
            print("Netrafil si ani jednu možnú voľbu. Musím sa ťa spýtať ešte raz.")
            continue
        if start_choice == "0":
           return  phase_constants.INTRO
        else:
            loaded,next_phase= load_game()
            if loaded:
                print(f"Hra sa naćitala, výtaj späť {hero_data.hero_name}")
                return phase_check(next_phase)
            else:
                continue