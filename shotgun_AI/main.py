"""
The MIT License (MIT)
Copyright (c) 2015 David Greydanus
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
'''           
Created on Dec 15, 2013
Overhauled  on Jan 22, 2015

@author: DavidGrey
'''

from random import choice
from ascii_art import *
from msvcrt import getwch
from states import game_states


clear = "\n" * 20


def get_values(state):
    """Takes a dictionary game state as inputs,
    extracts and returns the values of that dict in a tuple"""
    keys = ['player_ammo', 'player_block', 'player_prev', 'comp_ammo', 'comp_block', 'comp_prev']
    return tuple([state[key] for key in keys])


def get_move(state):
    """Takes a game state as input,
    returns a move based on locked bool values
    and states weights"""
    entry = game_states[get_values(state)]
    winners = []

    for move in entry:
        next = entry[move]
        if next == 'Y':
            return move
        elif next == 'N':
            continue
        winners += [move]*next
    else:
        return choice(winners)


def run_match(player_move, comp_move, state):
    """Takes 2 moves and a game state as input,
    updates the curr_state variable,
    returns the game_states entry for the modified state"""
    player_vul = False
    comp_vul = False
    state['player_prev'] = player_move
    state['comp_prev'] = comp_move

    #Update game variables
    if player_move == 'd':
        state['player_ammo'] += 1
        player_vul = True
    if comp_move == 'd':
        state['comp_ammo'] += 1
        comp_vul = True
    if player_move == 'a':
        if comp_vul:
            return 'N'
        state['player_ammo'] -= 1
    if comp_move == 'a':
        if player_vul:
            return 'Y'
        state['comp_ammo'] -= 1

    return game_states[get_values(state)]


def main(round = 0):
    print clear*2
    curr_state = {'player_ammo':1, 'player_block':True, 'player_prev':'d',
                   'comp_ammo':1, 'comp_block':True, 'comp_prev':'d'}
    lock = False
    player_blocks = 0
    comp_blocks = 0
    ascii = {'a':gun,
             's': shield,
             'd':reload,
             'Y':loss,
             'N':win}
    #Main loop
    while True:
        round += 1
        print 'Round '+str(round)+':\n'+' Your Bullets| ' + '*'*curr_state['player_ammo']+'\n My Bullets  | ' + '*'*curr_state['comp_ammo']+'\n'
        values = get_values(curr_state)
        #First move isn't pulled from game states
        if round > 1:
            #If guaranteed a win, the AI locks itself into firing mode 
            if curr_state['comp_ammo'] > (curr_state['player_ammo'] + (3-player_blocks)):
                comp_move = 'a'
                lock = True
            if not lock:
                comp_move = get_move(curr_state)
            else:
                comp_move = 'a'
        else:
            comp_move = choice(['a','s','d'])

        #Player selects move
        while True:
            print ":"
            player_move = getwch()# raw_input(":") #getwch()
            #Confirm player move is valid
            if player_move in ['a','s','d']:
                if player_move == 'a' and not curr_state['player_ammo']:
                    print 'You can\'t fire'
                    continue

                elif player_move == 's' and not curr_state['player_block']:
                    print 'You can\'t block'
                    continue

                elif player_move == 'd' and curr_state['player_ammo'] == 6:
                    print 'You can\'t reload'
                    continue
                break
            else:
                print clear+"Invalid input\n"+'Round '+str(round)+':\n'

        #Update block variables
        if player_move == 's':
            player_blocks += 1
            if player_blocks == 3:
                curr_state['player_block'] = False
        else:
            player_blocks = 0
            curr_state['player_block'] = True

        if comp_move == 's':
            comp_blocks += 1
            if comp_blocks == 3:
                curr_state['comp_block'] = False
        else:
            comp_blocks = 0
            curr_state['comp_block'] = True



        #Print match
        print clear + ascii[player_move] +'\n'*2 + ascii[comp_move] + '\n'

        result = run_match(player_move, comp_move, curr_state)

        #<Learning Code>
        if player_move == 'a':
            if game_states[values]['s'] not in [ 'N', 'Y']:
                game_states[values]['s'] += 1
            elif game_states[values]['a'] not in [ 'N', 'Y']:
                game_states[values]['a'] += 1

        elif player_move == 's':
            if game_states[values]['d'] not in [ 'N', 'Y']:
                game_states[values]['d'] += 1
            elif game_states[values]['s'] not in [ 'N', 'Y']:
                game_states[values]['s'] += 1

        elif player_move == 'd':
            if game_states[values]['a'] not in [ 'N', 'Y']:
                game_states[values]['a'] += 1
            elif game_states[values]['d'] not in [ 'N', 'Y']:
                game_states[values]['d'] += 1
        #<\Learning Code>


        if result in ['Y', 'N']:
            with open("states.py", "w") as states:
                states.write('game_states='+str(game_states))
            return ascii[result]
            input("stop")



if __name__ == '__main__':
    print main()
    while True:
        print "Press any key to play again"
        getwch()
        print main()
