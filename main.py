
INTRO_TEXT= "Práve si zapol hru Arkádius, v ktorej budeš bojovať proti príšerám a pri tom si zlepšuješ svojho hrdinu. Si na to pripravený?\n 0- Nie, bojím sa.\n 1-Áno poďme na to\n "


abilities = {
    "Útočná sila": {
        "points": 1,
        "description": "Sila je potrebna k útoku, do ktorého okrem sily vstupuje aj obratnosť a skill."
},
    "Obrana": {
        "points": 1,
        "description": "Celkový obrana sa ráta z bodov obrany +         obratnosti."
},
    "Obratnosť": {
        "points": 1,
        "description": "Obratnosť je dôležitá aj pre obranu aj pre útok."
},
    "Skill": {
        "points": 1,
        "description": "SKill je dôležitý pri normálnom útoku ako aj         kritickom útoku"
},
    "Život": {
        "points": 50,
        "description": "Život je dôležitý pri bitke. Život sa dá        doplniť po každom súboji."
    },
    "Šťastie": {
        "points": 1,
        "description": "Šťastie je dôležité pre kritický útok"
}
}



def print_abilities_points():
    for k,v in abilities.items():
        print(k+" - "+ str(v["points"]), end=", ")
    print("\n")

def print_abilities_options():
    for i, ability in enumerate(abilities.keys()):
        ability_option= str(i+1)+' - '+ability
        if ability=="Život":
            ability_option+=""+"- jeden bod pridáva 5 života"
        print(ability_option)

def hero_choice_abilitie():
    value= int(input(f"Máš {points} na zlepšenie. Ktorú schopnosť chceš vylepšiť?:"))
    return value



continue_game=True
while continue_game:
    print(INTRO_TEXT)
    #intro_choice=input("Aká je tvoja voľba?")
    intro_choice="1"
    if intro_choice not in["0","1"]:
        print("Netrafil si ani jednu s možnú voľbu. Musím sa spítať znovu")
        continue

    if intro_choice=="0":
        print("To ma mrzí. Dúfam, že prídeš aspoň neskôr")
        break

    print("Výborne, máš odvahu. To sa mi páči")
    name_picked = False
    hero_name = ""
    while not name_picked:
        name= "rasto"
        #name = input("Ako sa bude volať tvoj hrdina?: ")
        print("Si si istý, ze sa tvoj hrdina bude volať " + name + "?")
        print("0 - Nie, chcem zmeniť meno\n1 - Áno")
        name_choice="1"
        #name_choice = input("Aká je tvoja voľba?: ")
        if name_choice not in ["0", "1"]:
            print("Netrafil si ani jednu možnú voľbu. Musím sa ťa spýtať ešte raz.")
            continue
        if name_choice == "1":
            hero_name = name
            break
    print("Ahoj", hero_name)

    abilities_information= f"{hero_name}, Tvoje schopnosti sú momentálne na tom takto:"
    print(abilities_information)
    print_abilities_points()

    points = 7

    abilities_options = f" Máš {points} bodov, ktoré si rozdel naprieč schopnostiam podľa svojich preferencii."
    print(abilities_options)

    while continue_game:
        # f"Máš {points} na zlepšenie. Ktorú schopnosť chceš vylepšiť?
        chosen_ability_index = hero_choice_abilitie() - 1
        if 1 < points <= 7:

            abilities_index = (list(abilities.keys())[chosen_ability_index])
            points -= 1
            actualiy_condition="Teraz tvoje body vyzerarajú takto"

            if abilities_index== "Život":
                abilities[abilities_index]["points"] += 5
                print(f"Vybral si si možnosť - {abilities_index} pridávam ti 5 bodov.")
                print( actualiy_condition)
                print_abilities_points()
            else:
                 abilities[abilities_index]["points"] += 1
                 print(f"Vybral si si možnosť - {abilities_index} pridávam ti bod.")
                 print(actualiy_condition)
                 print_abilities_points()

        elif points==1:
            print(f"Výborne {hero_name}. Dokončil si pridávanie schopnosťí. Pre rekapituláciu, teraz vyzerajú tvoje schopnosti takto.")
            print_abilities_points()
            break
        else:
            print("Netrafil si ani jednu možnú voľbu. Musím sa ťa spýtať ešte raz.")



