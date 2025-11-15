# def say_number(n):
#     print(n)
#     if n < 8:
#         say_number(n+1)
# say_number(0)



def add_one(num):
    if(num >= 9):
        return num + 1
    total = num + 1
    print(total)
    
    return add_one(total)  #<---- function calling it self

add_one(0)



####### return tells a function to send back the value where it was called,and then stop running the function