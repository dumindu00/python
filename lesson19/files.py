import os

f = open("names.txt")
# print(f.read())
# print(f.read(4))
# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

# try:
#     f = open("names.txt")
#     print(f.read())
# except:
#     print("The file you want to read doesn't exist.")
# finally:
#     f.close()
    
########## Append - creates the file if doesn't exist

f = open("names.txt", "a")
f.write("Neil\n")
f.close()

f = open("names.txt")
print(f.read())
f.close()

#### Write (overwrite)
f = open("names.txt", "w")
f.write("I deleted all of the content")
f.close()

f = open("names.txt")
print(f.read())
f.close()

#### Two ways to create a new file

## Opens a file for writing, creates the file if it does not exist.

f = open("city_list", "w")
f.close()

## Creates the specified file, but returns an error if the file exists.

if not os.path.exists("some.txt"):
    f = open("some.txt", "x")
    f.close()
    

## Delete a file
## avoid an error if  it doesn't exist

if os.path.exists("some.txt"):
    os.remove("some.txt")
else:
    print("The file you wish to delete does not exist.")

with open ("context.txt") as f:
    content = f.read()

with open("names.txt", "w")  as f:
    f.write(content)