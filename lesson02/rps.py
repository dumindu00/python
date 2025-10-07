import sys
import random
from enum import Enum 



class RPS():
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:



 



    playerchoice = input('\n Enter... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n')

    player = int(playerchoice)

    if player < 1 | player > 3:
        sys.exit('enter a number in range 1-3')
        
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
        
    playagain = input("\nPlay again ? \nY for Yes or \nY for Yes or \n to Quit \n\n")
    
    if playagain.lower() == "y":
        continue
    else:
        print("\n hey")
        print("\n Thank you for playing!\n")
        playagain = False

sys.exit("Bye!....")