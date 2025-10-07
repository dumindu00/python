# def hello ():
#     print("Hello World!")


# hello()    

# def sum(num1, num2):
#     print(num1+num2)
    
# sum(2, 5)







# user  = input("Enter a number to start ")
# operator = input("Enter a operator form(+,-,*,%) ")
# user1 = input("Enter another number ")
# try:
#     num1 = int(user)
#     thing = operator
#     num2 = int(user1)
# except ValueError:
#     print('Enter valid number!')
#     exit()


# def magic(num1, thing, num2):
        
#         if thing == "+":
#             print(num1 + num2)
#         elif thing == "-":
#             print(num1 - num2)
#         elif thing == "*":
#             print(num1 * num2)
#         elif thing == "%":
#             print(num1 % num2)
#         else:
#             print("enter valid operator!")
    
# magic(num1, thing, num2)

def names(*args):
    print(args)
    

listofnames=("Viraj", "Dumindu", "Sunny")

names(listofnames)