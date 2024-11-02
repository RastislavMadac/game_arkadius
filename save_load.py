import hero_data

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
            file_handler.close()
            print("Úspešne som uložil hru.")
            print()
            break
        else:
            print("Tvoj súbor neobsahuje iba písmena. Skús ešte raz pos iným názvom")
            continue
