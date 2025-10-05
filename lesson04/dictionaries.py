# Dictionaries

band = {
    "vocals": "Plant",
    "guitar": "Page",
    "members": 2
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band2))

print('')

# Access items
print(band.keys()) # Return keys
print(band.values()) # Return values
print('')


print(band["guitar"])

print(band.get("guitar")) # access values

print(band.items()) # list of key/values pairs as tuples
print('')
print("guitar" in band) # verify if key exists
print("members" in band) # verify if key exists

print('')

# Change values
band["guitar"] = 'Adrian'
band.update({"drum": "BJJ"})
print(band)

# remove items
print(band.pop('vocals'))
print(band)

band['piano'] = "ATJ"
print(band)

print(band.popitem())
print(band)

# Delete
band['piano'] = "ATJ"
del band["piano"]
#band.clear()   # clear whole dictionary
print(band)
print('')

# Copy dictionary
some ={
    "F1": "ferrari",
    "motogp": "honda",
    "gt": "ford"
}

some2 = {
    "italy":"lamborghini",
    "german":"BMW",
    "england":"RR"
}
del some


# Create reference

# some = some2 # create reference
# print("Bad Copy!")
# print(some)
# print(some2)

# some["football"] = "cr7"
# print(some2) 



some = some2.copy()
some["football"] = "cr7"
print("Good Copy!")
print(some2)
print(some)

# or 
some3 = dict(some2)
print("Good Copy!")
print(some3)
print('')
# Nested Dictionary
actor = {
    'taken': 'liam',
    'reOne': "rayan",
}
sport = {
    'football': "messi",
    'MMa': "cornar"
}
merge = {
    "actor": actor,
    "sport": sport
}

print(merge)
print(type(merge))

print(merge["actor"]["taken"])

print('')
##############--- SETS ---############
nums = {1,2,3,4,5}
nums2 = set((6,4,2))

print(type(nums))
print(type(nums2))
print(len(nums2))

# N0 duplicate allowed
nums =  {1,2,3,4,4,5}
print(nums)

# True and False
new = {1, True, 9, 0,False}
print(new)

print(1 in new)
print(True in new)
print(0 in new)
print(False in new)

# can't refer to an element in the set with an index position or a key
# Adding
new.add(5)
print(new)
# new.clear()
new.remove(9)
print(new)

# add sets
new2 = {8,4,2,5}
new.update(new2)
print(new)

print('')
# Merge
one = {1,2,4}
two = {5,2,1}

three = one.union(two)
print(three)

# to keep duplicates
one.intersection_update(two)
print(one)

# except duplicate
one.symmetric_difference_update(two)
print(one)