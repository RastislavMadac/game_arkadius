import hero_data
from os import listdir
import game_constants

def save_game(phase):
    print("Pod akým názvom chceš uložiť hru?(Názov nesmie obsahovať špeciálne znaky, čísla a medzeri")
    while True:
        save_name= input("Názov - ")
        if save_name.isalpha():
            #save_file
            file_path= "saved/" + save_name + ".txt"
            file_handler= open(file_path, "w", encoding="utf-8")
            file_handler.write(hero_data.hero_name+ "\n")
            for k,v in hero_data.abilities.items():
                 file_handler.write(k + " - " +str(v["points"]))
                 file_handler.write("\n")
            file_handler.write(phase + "\n")
            file_handler.write(str(hero_data.available_points))
            file_handler.close()
            print("Úspešne som uložil hru.")
            print()
            break
        else:
            print("Tvoj súbor neobsahuje iba písmena. Skús ešte raz pod iným názvom")
            continue


def load(file):
    print(f"Načitávam hru uloženú pod názvom {file.replace('.txt', '')}")

    file_handler= open("saved/" + file, "r", encoding="utf-8")

    name_loaded=False
    abilities_loaded =False
    abilities_loaded_counter=0
    next_phase_loaded=False
    next_phase=""
    avalaible_points=False

    for line in file_handler:
       line = line.rstrip()
       if not name_loaded:
          hero_name=line
          hero_data.hero_name=hero_name
          name_loaded=True
       elif not abilities_loaded:
           ability_key, points= line.split(" - ")
           hero_data.abilities[ability_key]["points"]=int(points)
           abilities_loaded_counter+=1
           if abilities_loaded_counter==len(hero_data.abilities):
               abilities_loaded=True
       elif not next_phase_loaded:
           next_phase=line
           next_phase_loaded=True
       elif not avalaible_points:
           hero_data.available_points=int(line)
           avalaible_points = True
    return True, next_phase



def load_game(): # Returns tuple(boolian. string) ci sa podarilo načítať hru a string he nayov fazy, v ktorej pokračuje hra
    saved_file=[]

    for file in listdir("saved"):
       saved_file.append(file)


    if len(saved_file)>0:
        print("0 - Späť")
        print(game_constants.DIVIDER)
        for i, save in enumerate(saved_file):
            list_number=str(i+1)
            print(f"{list_number}. - {save.replace('.txt', '')}")
        print(game_constants.DIVIDER)

        while True:
            choice =input("Aký súbor chceš načítať?")
            if choice =="0":
                return False,""

            if not choice.isdigit() or int(choice) not in list(range(1, len(saved_file) + 1)):
            #if choice not in list_number:
                print("Netrafil si ani jednu možnosť. Pýtam sa ešte raz")
                continue
            else:
                game_to_load= saved_file[int(choice)-1]
                return load(game_to_load)
    else:
        print("Nemáš žiadne uložené hry")
        return False, ""