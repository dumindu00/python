# string
firstName = "Dumindu"
lastName = 'Viraj'
age = 25
foods = ['pizza', 'lasagna', 'pasta']


print(type(firstName))
print(type(age))
print(type(foods))

# constructor function

subject = str("Engineering")
print(type(subject))
print(isinstance(subject, str))


# Concatenation

fullName = firstName + ' ' + lastName
print(fullName)

# Casting number to string
toStringAge = str(age)
number = str(119947484)
print(fullName + ' ' +toStringAge)

welcome = 'I am ' + fullName + ' call me on ' + number + "."
print(welcome)



# Multiple lines
multiline = '''hey, how are you? 
    i am dv.
    is everything ok?
    
    can i help you with anything?
'''
print(multiline)


# escaping special characters
sentence = '''I\'m dv, arn\'t you the new guy?
i don\'t remember you that much'''
print(sentence)



# String methods

words = 'hey i am GOOD at PYTHON!'

print(words)
print(words.lower())
print(words)
print(words.upper())

print(words.title())


print(words.replace('PYTHON', 'JAVASCRIPT'))


print(len(words))
print(len(sentence))


print('')



# Build A simple menu
heading = "vito\'s menu".upper()
print(heading.center(20, '='))
print('')
print('Coffee'.ljust(20, "-")+ ' $3.50'.rjust(4))
print('Pizza'.ljust(20, "-")+ ' $5.20'.rjust(4))
print('HotDog'.ljust(20, "-")+ ' $2.30'.rjust(4))
print('Burger'.ljust(20, "-")+ ' $2.00'.rjust(4))

print('')

# string index values
some = 'it is was  beautiful experience'

print(some[0])
print(some[-1])
print(some[1:-1])

print("")


# Boolean data types
value = True
value1 = bool(False)
print(type(value1))
print(isinstance(value, bool))

print("")

# Numerical data types
price  = 100
price1 = int(90)
print(type(price1))
print(isinstance(price, int))
print("")

# float type

gpa = 3.28
average = float(45.6)
print(type(average))
print(isinstance(gpa, float))
print("")


# complex numbers
comp_num = 4+6j
comp_num1 = complex(4j+-3)
print(type(comp_num1))
print(isinstance(comp_num1, complex))
print(comp_num.real)
print(comp_num.imag)

print("")

# Built-in functions for numbers
print(abs(gpa))
print(gpa * -2)

print(round(gpa))
print(round(gpa, 8))


print("")

# for further math import math modules

import math

count = 4.6


print(math.pi)
print(math.sqrt(count))
print(math.ceil(count))
print(math.floor(count))
print("")

# casting string to a number
code = "678764"
toInt = int(code)
print(type(toInt))
