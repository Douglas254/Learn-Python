# TUPLES are read only and use parenthesis ()
# SIMILAR TO LIST;
# they are immutable, cannot be edited, added


# concatenate tuple
point = (1, 2, 3) + (4, 5, 6)
print(point)

# accessing tuple using indexes
numbers = (2, 4, 6, 8, 10)
print(numbers[:2])
print(numbers[4])
print(numbers[::3])

# converting a list to a tuple
list1 = [3, 4, 5, 6, 7]
print(tuple(list1))

numbers = (2, 4, 6, 8, 10)
numbers[0]  # accessing elements
# numbers[0] = 10  # Type Error , they cannot be edited / not support item assignemnt

# UNPACKING
numbers = (2, 4, 6)

# check if a number exist in a tuple or not
if 10 not in numbers:
    print("doesn't exist")

# Accessing from indexing and multiplying
multiply = (numbers[0]*numbers[1]*numbers[2])
print(multiply)  # 48 but tedious code

# assign new var
x = numbers[0]
y = numbers[1]
z = numbers[2]
print(x*y*z)  # 48

# with unpacking
x, y, z = numbers
print(x*y*z)  # 48
