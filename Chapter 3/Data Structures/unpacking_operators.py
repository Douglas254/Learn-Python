numbers = [1, 2, 3, 4]
print(*numbers)

# unpacking iterables
values = [*range(5)]
print(values)


first = [2, 3]
second = [4, 5]
combined = [*first, "a", * second, *"hello"]
print(combined)

# unpacking dictionary operaators
dict1 = {"X": 1}
dict2 = {"X": 10, "Y": 2}
combined = {**dict1, ** dict2, "Z": 1}
print(combined)  # multiple value with the same key the last value will be used
