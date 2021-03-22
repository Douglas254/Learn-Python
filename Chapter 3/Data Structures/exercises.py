
# 1. program to find the most repeated charcter in this text >>> "This is a common interview question"
from pprint import pprint

sentence = "This is a common interview question"
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# pprint(char_frequency, width=1) # using the pprint function
char_frequency_sorted = sorted(
    char_frequency.items(), key=lambda kv: kv[1], reverse=True)  # kv i.e a key value pair in dict
print(char_frequency_sorted[0])


# 2. Write some code that creates a list of integers ,loops through each element of a list and prints out the even numbers in the list
listofNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in listofNumbers:
    print(number),
    if number % 2 == 0:
        print("is even")
    else:
        print("is odd")
