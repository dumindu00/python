### Closure is a function having access to the scope it's parent
### after the parent function has returned.

def parent_function(person, coins):
    # coins = 3
    
    def the_game():
        nonlocal coins
        coins -= 1
        
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        else:
            print("\n" + person + " has no coins left.")
        
    return the_game

sara = parent_function("Sara", 40)
dumindu = parent_function("dumindu", 4000)

dumindu()

sara()

