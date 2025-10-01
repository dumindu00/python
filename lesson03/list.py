users = ["Dave", "Dumindu", "Sara"]
data = ['Dumindu', 25, True]

emptylist= []


print("Dumindu" in emptylist)
print(users[-1])

print(users.index("Sara"))


print(users[0:2]) # This will print position 0,1 and position 2 will not be included.

print(len(data))

data.append("Bunny") # Add item to list.
users.append(8)  # Add item to list.
print(data)
print(users)


users += "Pizza" # Adds each character separately
data += ["Viraj"] # Adds as it is to list number /string
print(users)
print(data)

print('')

#data.extend(["Batman", "Superman", "Robin"])        # can add new list to list
# print(data)

users.extend(data) # adds existing lists
# print(users)


data.insert(3, "Mr.Bean")
print(data)
print('')
data[2:2] = ['The Rock','Bob']
print(data)

data[2:3] = ["JAKE", "TERRY"]
print(data)

print('')

 # Removing items from List

print(data)
data.remove(25)
data.remove("TERRY")
print(data)


print("")

print(data.pop())
print(data)

del data[3]
print(data)

# users.clear()  # clear list items list remain
# print(users)

users.remove(25)
users.remove(8)
users.remove(True)

print(users)
users.sort()
print(users)

# users.sort(key=str.lower)
# print(users)

print('')

nums = [4, 42, 62, 1, 3]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

print('')
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(nums)
print(numscopy)
numscopy.sort()
print(numscopy)
print(mynums)
print(mycopy) 

print(type(nums))

mylist = list([1, "car" , "train"])
print(mylist)


print('')
print('')


########## TUPLES ############## tuples are like list but the data inside will not change and the order too. 

mytuple = tuple(("Viraj", 4, True))
tuple2 = (1,2,3,4, 4,4)

print(mytuple)
print(type(tuple2))


newlist = list(mytuple)
newlist.append('Sara')
print(type(newlist))
newmytuple = tuple(newlist)
print(newmytuple)
print(type(newmytuple))


# unpack tuple

(one, *two, hey) = tuple2
print(one)
print(two)
print(hey)

print(tuple2.count(4)) # Returns the number of occurrence 
