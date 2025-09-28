import sys
import random

print('')

playerchoice = input('Enter... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n')

player = int(playerchoice)

if player < 1 | player > 3:
    sys.exit('enter a number in range 1-3')
    
computerchoice = random.choice("123")

print('You chose: ' + playerchoice + ".")
print("Computer chose :" + computerchoice + ".")
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