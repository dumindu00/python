# value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# value = 1
# while value <= 10:
#     value+= 2
    
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))

# names = ['Dave', 'Sara', 'John']
# for i in names:
#     print(i)
    
# for i in "Mississippi":
#     print(i)

# for x in names:
#     if x == 'John':
#         break
#     print(x)

# for x in names:
#     if x == "Sara":
#         continue
#     print(x)


# for x in range(4):
#     print(x)

# for x in range(0, 10, 2):
#     print(x)
# else:
#     print("counting is over!")



names = ['Dave', 'Sara', 'John']
actions = ["eats", "codes, sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")
        
