class JustNotCoolError(Exception):
    pass




try:
    raise JustNotCoolError("I am custom not cool exception")
    # x = 2
    # y = q
    # def add(x, y):
    #     print(x+y)
    # add(x,y)
    # if not type(y) is str:
    #     raise TypeError("Only st are allowed")
except NameError:
    print(" something wrong!")
except Exception as error:
    print(error)
else:
    print("No errors!")
    
finally:
    print("any way I am going to print with or without an error!")