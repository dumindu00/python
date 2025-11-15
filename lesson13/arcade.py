import sys
from rps import rps
from guess_number import play_guess_number



def play_game(name="PlayerOne"):
    welcome_back = False
    
    while True:
        if welcome_back == True:
            print(f"\n {name}, welcome back to the Arcade menu..")
        
        playerchoice = input(
            "\nPlease choose a game: \n 1.Rock & Paper Scissors\n2.Guess the Number\n\n or press \"x\" to exit the Arcade."
        )
        
        if playerchoice not in ["1", "2", "x"]:
            print(f"\n{name}, please enter 1,2,3 or X.")
            return play_game(name)
        
        welcome_back = True
        
        
        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == "2":
            guess_number = play_guess_number(name)
            guess_number()
        else:
            print("\n See you next time!\n")
            sys.exit(f"Bye {name}!")


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
    print(f"\n{args.name}, welcome to the Arcade!")
    
    play_game(args.name)
    
    
