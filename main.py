
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





