import sys
import random




def play_guess_number(name='PlayerOne'):
    game_count = 0
    player_wins = 0




    def guess_number():
        nonlocal name
        nonlocal player_wins
        
        
        playerchoice = input(f"\n{name}, guessed the number i am think of!...😁😊")
        
        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, enter 1, 2, or 3 to play.")
            return guess_number
        
        computer = random.choice("123")
        
        print(f"\n{name}, you chose {playerchoice}.")    
        print(f"I was thinking {computer}.\n")    
        
        player = int(playerchoice)
        computerchoice = int(computer)

        def game_logic():
            
            nonlocal name
            nonlocal player_wins
            
            if player == computerchoice:
                player_wins += 1
                return f"🥳😱{name} guessed it right..!"
            else:
                
                return f"😅 Sorry {name}!. Better luck next time.😐"

        game_result = game_logic(player, computerchoice)

        print(game_result)
        nonlocal game_count
        game_count += 1
        
        print(f"\n Game count: {game_count}")
        print(f"\n {name}' wins: {player_wins}")
        print(f"\n Winning percentage: {player_wins / game_count :.2%}")
        
        
        print(f"\n Wanna try again {name}???😎🙃🙂\n")


        while True:
            playagain = input(f"\n Y for yes and Q for quit\n")
            if playagain.lower() not in ["y","q"]:
                continue
            else:
                break
            
        if playagain.lower() == "y":
            return guess_number()
        else:
            if __name__ == "__main__":
                sys.exit(f"Good Bye..{name}!!!😏🙁🥺")
            else:
                return


        return guess_number


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
    guess_my_number = play_guess_number(args.name)
    guess_my_number()
    
    
    
# build a math game that calculate circumference, pythagoras, and area of rectangle..