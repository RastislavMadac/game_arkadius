import game_constants
import phase.phase_constants as phase_constants
from phase.abilities import abilities_update
from phase.intro import intro_phase
from phase.name import name_phase
from phase.check import phase_check
from phase.start import start_phase

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
        print("Si pripravený na prvý súboj?")
        break


