import math

# print Hello world to the screen

print("Hello World")

# Variables - Memory location in the computer where data is stored
# Variables should be descriptive and meaningful for more maintainable of the code
# Primitive Types in python i.e Numbers, Boolean & Strings

students_count = 1000
rating = 4.99  # Floating numbers
is_published = True  # Boolean
author_name = "Douglas254"  # Strings you can either use "" 0r ''

# Strings
# Function is a container that holds pieces of code defined to do a specific task and are reusable

course = "Python Programming"
message = """
Hi, Developers
let's learn some amazing tips in python
Regards
Douglas254
"""
print(len(message))  # len() function finds the length of the string
print(course[0])  # prints the first character of the string
print(course[-1])  # Prints the last character of the string

# slicing [index:index]
# Prints the first three characters starting from index 0 to 2

print(course[0:3])
print(course[0:])  # prints the whole character

# Prints the first three characters starting from index 0 to 2

print(course[:3])
print(course[:])  # Prints the whole character string
new_name = course[:]  # copies contents of the string to the new-string name
print(new_name)

# Escape Sequences i.e \", \', \\, \n
# Escaping character \ and Escape sequence \", \', \\, \n

course = "Python \"programming"
print(course)

# Formatting Strings
# String Concatenation

first = "Douglas"
last = "Obara"
full = first + " " + last
print(full)

# F string formatting

full = f"{first} {last}"
print(full)

# String Methods

course = "  python programming"
print(course.upper())
print(course.lower())
print(course.title())  # Capitalize the fist letter of every word
print(course.strip())  # Removes white spaces with rstrip or lstrip

# finds the index of the specified word and if not found return -1 no char

print(course.find("pro"))
print(course.replace("p", "r"))  # Replaces p with r

# check if element/char exist in a char
# returns a boolean value , if misspelled returns false.

print("pro" in course)  # return True
print("swift" not in course)  # return True
print("Pro" in course)  # return False

# Arithmetic Operations

print(5 + 3)  # Addition
print(5 - 3)  # subtraction
print(5 * 3)  # multiplication
print(5 / 3)  # floating value
print(5//3)  # returns only whole numbers
print(5 % 3)  # returns remainder
print(5**3)  # returns the power of a number

# Incrementing/Decrementing Values

i = 3
i = i + 3
print(i)  # return 6

i += 3
print(i)  # return 9 after incrementing 6 by 3

i -= 3
print(i)  # return 6 after decrementing by 3 ,i-=3 is same as i = i - 3.

# Working with Numbers

print(round(3.7))  # round off a number to the nearest whole number
print(abs(-3.7))  # Returns a positive integer

# Math Function

i = 6.3
print(math.ceil(i))
print(math.floor(i))

# Type conversion i.e int(),float(),str(),bool()
x = input("X: ")
y = int(x) * 2
print(f"X: {x} , Y: {y}")

# Falsy values
# ""
# 0
# None

print(bool(""))
print(bool(0))
print(bool(None))

# comparison operators - they are used to compare values
# >  # Greater than
# >=  # Greater than or equal to
# <  # Less than
# <=  # Less than or equal to
# ==  # Equality operator
# !=  # Not equal operator


# Conditional statements
# if statement

temperature = 35
if temperature > 30:
    print("It's Warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")  # This statement will execute whether the condition is true or not

# Ternary Operator
age = 24
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

# Logical Operators
# AND Operator - if both operators are true the result will be true
high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")

# OR Operator - if one of the condition is true the result will be true
high_income = False
good_credit = True

if high_income or good_credit:
    print("Eligible")
else:
    print("Not Eligible")

# NOT Operator
high_income = False
good_credit = True
student = False

if not student:
    print("Eligible")
else:
    print("Not Eligible")

# Combining all operators in complex
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")

# Short circuit evaluation
high_income = True
good_credit = True
student = True

if high_income and good_credit and not student:
    print("Eligible")
else:
    print("Not Eligible")

# Chaining comparison operators
# age should be between 18 and 65
age = 22
if 18 <= age < 65:  # same as age >= 18 and age < 65
    print("Eligible")

# Looping
# FOR Loop
for number in range(1, 10, 2):
    print("Attempt", number, number * "*")

# FOR ELSE Loop
successful = True  # When False the else statement will be executed
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# Nested Loop
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# Iterable
for x in "python":
    print(x)

# While Loop
command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

# Infinite Loop - Loops that run forever
while True:
    command = input(">")
    print("ECHO", command)
    break  # we use the break keyword to terminate the loop

#  Program to display even numbers between 1 to 10 and display message "We have 4 even numbers"
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        count = count + 1
print(f"We have {count} even numbers")
