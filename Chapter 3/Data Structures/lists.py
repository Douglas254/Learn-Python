# lists uses square brackets []
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters
numbers = list(range(20))
chars = list("Hello World")
print(chars)

# Accessing items in list
print(letters[0])  # prints the first index

# modifying items in list
letters[0] = "A"
print(letters)

# reverse list
numbers = list(range(20))
print(numbers[::-1])

# unpacking lists
numbers = [1, 2, 3]
first, second, third = numbers  # unpacking
print(first)
print(second)
print(third)

# packing list
numbers = [1, 2, 3, 4, 4, 5, 3, 8, 9, 5]
first, second, *others = numbers  # * used for packing the remaining item in list
print(first)
print(second)
print(others)

# looping over list
letters = ["a", "b", "c"]
for letter in letters:
    print(letter)

for index, letter in enumerate(letters):
    print(index, letter)

# adding/removing items in list
letters = ["a", "b", "c", "d"]

# add
letters.append("e")  # adds at the end of the list
letters.insert(0, "-")  # adds at a specified index
print(letters)

# remove
letters.pop(0)  # remove item at a specified index
letters.remove("b")
del letters[0:3]  # remove a range of item
letters.clear()  # remove all in the list
print(letters)


# sorting lists
numbers = [3, 51, 8, 6, 32, 4]
numbers.sort()  # sort in ascending order and numbers.sort(reverse=True) - descending order
print(numbers)
print(sorted(numbers))  # sames as numbers.sort()

# using lambda to sort list
items = [
    ("product 1", 10),
    ("product 2", 9),
    ("product 3", 12),
]

items.sort(key=lambda item: item[1])
print(items)


# Challenge
# write a program to remove duplicate elements in a list and arrange the numbers in descending order

numbers = [2, 3, 4, 5, 6, 2, 4, 7, 8, 4, 9]
new_list = []

for x in numbers:
    if x not in new_list:
        new_list.append(x)
        new_list.reverse()
print(new_list)


# challenge
# write a program to return largest values in a list

numbers = [9, 4, 6, 12, 9, 4, 3, 1, 8]
largestNumber = numbers[0]
for number in numbers:
    if number > largestNumber:
        largestNumber = number
print(largestNumber)
