

print('')

menu = print("""Here is today's Vito's menu\n
    ****Welcome to Vito's****
    
        Pizza  ---- e3.50
        Coffee ---- e1.25
        Pasta  ---- e2.50
        Lasagna --- e3.00
        Burger ---- e1.25
        HotDog ---- e1-00
            """)
print('')

menu1 = {
    'Pizza': 3.50,
    'Coffee':  1.25,
    'Pasta' : 2.50,
    'Lasagna': 3.00,
    'Burger': 1.25,
    'HotDog': 1.00
}




# print('')
# if user in menu1:
#     print(f'Your total {user}: e{menu1[user]}')
# else:
#     print("Sorry! Item not in todays menu")
total_amount = 0
while True:
    user = input("Type your favorites and hit enter \n\n\n").title()

    
    
    if user == "":
        break 
    if user in menu1:
        quantity = int(input(f"Enter the quantity of {user} "))
        total = menu1[user] * quantity
        total_amount += total
        print(f"Added {quantity} * {user} = ε{total}")
    else:
        print("Item not in todays menu!")

print('')

print("***Total Bill***")
print(f"Your total amount is ε{total_amount}")