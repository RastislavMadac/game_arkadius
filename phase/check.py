
import phase.phase_constants as phase_constants

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



def phase_check(next_phase):
    while True:
        print("0 - Pokračovať na", next_phase)
        print("1 - Upraviť hrdinu")
        print("2 - Uložiť hru")
        print("3 - Ukončiť hru")

        choice=input("Aký je tvoj další krok?")
        if choice not in ["0", "1", "2", "3"]:
            print("Netrafil si ani jednú možnú voľbu. Musím sa ťa spýtať ešte raz")
            continue

        if choice =="0":
           return next_phase
        elif choice =="1":
            # TODO hero_check
            continue
        elif choice =="2":
            #TODO save_game
            continue
        elif choice =="3":
            if end_game_choice():
                return phase_constants.END
            else:
                print()
                continue


    # print_check_points()
    # check_points= False
    # while not check_points:
    #     option=str(input("Vyber si jednu z možností: "))
    #     if option==0:
    #        return next_phase
    #     elif option == 1 or option==2:
    #         continue
    #     elif option==3:
    #         print("Si si istý že chceš ukončiť hru?\n 0 - Späť \n 1 - Áno, ukončiť")
    #         end_game=input("Naozaj ukončiť? ")
    #         if end_game==0:
    #             continue
    #         elif end_game==1:
    #             print(DIVIDER)
    #             print("Dovidenia")
    #             break
    #     else:
    #         print("Netrafil si ani jednu možnú voľbu. Musím sa ťa spýtať ešte raz.")
    #         continue







