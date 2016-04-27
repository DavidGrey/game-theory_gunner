from os import _exit
from states import game_states

while True:
    confirm_reset = raw_input("""\nAre you sure you want to reset the game states?\n
Doing so will erase everything the AI has learned while playing.\n
Erase everything? Y/n: """)
    
    if confirm_reset.upper() == 'Y':
        break
    elif confirm_reset.upper() == 'N':
        print("\n\nReset canceled")
        _exit(0)
     

moves = ['a','s','d']

for state in game_states:
    for move in moves:
        if type(game_states[state][move]) == int:
            game_states[state][move] = 1


    
with open("states.py", "w") as states:
    states.truncate()
    states.write('game_states='+str(game_states))
    states.close()

print("\n\nReset complete")

