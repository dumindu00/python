import sys
import random
from enum import Enum 

def rps(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    computer_wins = 0


    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3
            

        playerchoice = input(f'\n {name}, Enter... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n')

        if playerchoice not in ["1", "2", "3"]:
            print(f'{name}, Enter a number in range 1-3')
            return play_rps()

        player = int(playerchoice)
            
            
        computerchoice = random.choice("123")
        comp = int(computerchoice)
        
        print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"\nComputer chose {str(RPS(comp)).replace('RPS.', '').title()}.\n")
        print('')

        def decide_winner(player, comp):    
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins
            if player == comp:
                return "game draw"
            elif player == 1 and comp == 2:
                player_wins += 1
                return f"{name}, you win!..🥳🤑"
            elif player == 3 and comp == 2:
                player_wins += 1
                return f"{name}, you win!..🥳🤑"
            elif player == 1 and comp == 3:
                player_wins += 1
                return f"{name}, you win!..🥳🤑"
            else:
                computer_wins += 1
                return f"🤣..Computer wins!\n try next time, {name}...😏😒"
            
        game_result = decide_winner(player, comp)
        
        print(game_result)
        
        nonlocal game_count
        game_count += 1
            
        print(f"\nGame count:  {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nComputer wins: {computer_wins}")
            
        print(f"\nPlay again, {name}..🙄🥺?")
        
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
            sys.exit(f"Bye {name}!...😪😓😢🖐")

    return play_rps


if __name__ == "__main__":
    
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal game experience."
    )   
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )
    

    args = parser.parse_args()
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()