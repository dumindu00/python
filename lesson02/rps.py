import sys
import random
from enum import Enum 



def play_rps():

    class RPS():
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
        

    playerchoice = input('\n Enter... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n')

    if playerchoice not in ["1", "2", "3"]:
        print('Enter a number in range 1-3')
        return play_rps()

    player = int(playerchoice)
        
        
    computerchoice = random.choice("123")

    print('\nYou chose: ' + playerchoice + ".")
    print("Computer chose :" + computerchoice + ".\n")
    print('')

    comp = int(computerchoice)

    if player == comp:
        print('game draw')
    elif player == 1 and comp == 2:
        print('player won')
    elif player == 3 and comp == 2:
        print('player won')
    elif player == 1 and comp == 3:
        print('plyer won')
    else:
        print('computer won')
        
        
        
    print("\nPlay again ?")
    
    while True:
        playagain = input(" \nY for Yes or \n to Quit \n\n")
        if playagain.lower() not in ['y', 'q']:
            continue
        else:
            break
    if playagain == 'y':
        return play_rps()
    
    else:
        print("\n hey")
        print("\n Thank you for playing!\n")
        sys.exit("Bye!....")




play_rps()