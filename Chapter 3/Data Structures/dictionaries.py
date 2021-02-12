# # Dictionary
"""
 Elements are enclosed in curl brackets "{}"

 Each key has a value pair separeted by full colon

 Does not allow repetative keys

 Empty dictionary are represented by opening and closing curl bracket alone

 Keys onces declared are immutable

 values can change in data type but keys must be in a string

 Formart:

     dict = {"key-element: value-element"}

     emptyDict = {}

# # Accessing values:

 We use keys to access values of a dictionary

 Accessing a value not in the dictionary throws a "Key Error"

 print("My name is :", dit['Name'])

# # Updating Dictionary

 updating can be perfomed by:

     adding complete new entry

     adding a key-value pair

     Modify existing entry

     Delete existing entry

     one element at a time

     delete entire dictionary

# # Properties of a dictionary

 Keys with more than one entry is not allowed

 No duplicate keys

 Repeated keys will take the last value placed and leave the first assigned value

 Keys are immutable:

     keywords are not used as keys

     other data types can be used as keys """


# Dictionaries - a collection of key value pairs

dict1 = {"Name": "Douglas254", "age": 87,
         "country": "Kenya", "Job": "tech_Company"}
print(dict1)

# we can use dict() function to display dictionaries
point = dict(x=1, y=2)  # key word arguments
print(point)


# adding a new key to the dictionary
point["z"] = 3
print(point)  # {'x': 1, 'y': 2, 'z': 3}


# accessing elements
for key in dict1:
    print(key, dict1[key])


# modifying elements of a dictionary
dict1["age"] = 24  # updating existing data
dict1["job"] = "Developer_Company"  # adding a new entry


# deleting
dict1.clear()  # removes all elements in a dictionary
print(dict1)  # {}

dict1 = {"Name": "Douglas254", "age": 87,
         "country": "Kenya", "Job": "tech_Company"}

del dict1["Name"]  # Removes elements
print(dict1)  # {'age': 87, 'country': 'Kenya', 'Job': 'tech_Company'}

del dict1  # deletes an entire dictionary


# single line comment
""" multi
          line
                 comment"""


# Dictionary comprehension
values = {}
for x in range(5):
    values[x] = x * 3
print(values)

# comprehension
values = {x: x * 3 for x in range(5)}
print(values)  # {0: 0, 1: 3, 2: 6, 3: 9, 4: 12}
