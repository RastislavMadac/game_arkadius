
INTRO_TEXT= "Práve si zapol hru Arkádius, v ktorej budeš bojovať proti príšerám a pri tom si zlepšuješ svojho hrdinu. Si na to pripravený?\n 0- Nie, bojím sa.\n 1-Áno poďme na to\n "

continue_game=True

while continue_game:
    print(INTRO_TEXT)
    intro_choice=input("Aká je tvoja voľba?")
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
        name = input("Ako sa bude volať tvoj hrdina?: ")
        print("Si si istý, ze sa tvoj hrdina bude volať " + name + "?")
        print("0 - Nie, chcem zmeniť meno\n1 - Áno")
        name_choice = input("Aká je tvoja voľba?: ")
        if name_choice not in ["0", "1"]:
            print("Netrafil si ani jednu možnú voľbu. Musím sa ťa spýtať ešte raz.")
            continue
        if name_choice == "1":
            hero_name = name
            break
    print("Ahoj", hero_name)