import game_constants
import hero_data
import phase.phase_constants as phase_constants


from phase.abilities import abilities_update
from phase.intro import intro_phase
from phase.name import name_phase
from phase.check import phase_check,battle_check
from phase.start import start_phase
from fight.battle import battle


current_phase = phase_constants.START



continue_game = True
while continue_game:

    if current_phase==phase_constants.START:
        current_phase=start_phase()
    elif current_phase==phase_constants.INTRO:
        current_phase=intro_phase()
    elif current_phase== phase_constants.END:
        print(game_constants.DIVIDER)
        print("Dovidenia")
        continue_game = False
    elif current_phase==phase_constants.NAME:
        print(game_constants.DIVIDER)
        current_phase=name_phase()
    elif current_phase == phase_constants.INTRO_ABILITIES:
        print(game_constants.DIVIDER)
        abilities_update(game_constants.INTRO_ABILITIES_COUNT)
        print(game_constants.DIVIDER)
        current_phase = phase_check(phase_constants.FIGHT)
    elif current_phase == phase_constants.FIGHT:
        print(game_constants.DIVIDER)
        is_boss_fight= hero_data.fight_level == game_constants.BOSS_FIGHT_LEVEL
        win, health_remining= battle(hero_data.fight_level)

        if win:
            if is_boss_fight:
                current_phase=phase_constants.WON_GAME
                continue
            #Bojovník vyhral
            print(f"Po výťaznej bitke ti ostal život {str(health_remining)} / {str(hero_data.abilities['Život']['points'])}")
            print(game_constants.DIVIDER)
            print(f"Po tvojej {str(hero_data.fight_level)} výhre ti pridávam {str(hero_data.fight_level)} body ktoré môžeš použiť na upravenie svojho hrdinu. ")
            abilities_update(hero_data.fight_level)
            hero_data.fight_level+=1
            is_boss_fight= hero_data.fight_level==game_constants.BOSS_FIGHT_LEVEL
            print(game_constants.DIVIDER)
        else:
            print(f"Potrebuješ si oddýchnuť a možno aj prehodnotiť svoje schopnosti, máš {hero_data.abilities['Život']['points']} života")
            print(game_constants.DIVIDER)

        max_health=hero_data.abilities["Život"]["points"]
        hero_data.abilities["Život"]["points"] = health_remining
        current_phase= battle_check(hero_data.fight_level, max_health)

    elif current_phase == phase_constants.WON_GAME:
        print(game_constants.DIVIDER)
        print("Porazil si posledného súpera, prešiel si celú hru. Gratulujem!!!")
        break