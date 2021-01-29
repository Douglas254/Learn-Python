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
# finds the index of the specified word and if return -1 no char
print(course.find("pro"))
print(course.replace("p", "r"))  # Replaces p with r
# check if element/char exist in a char
# returns a boolean value , if misspelled returns false.
print("pro" in course)  # return True
print("swift" not in course)  # return True
print("Pro" in course)  # return False


