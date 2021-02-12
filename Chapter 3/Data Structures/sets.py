
# sets - unordered collections of unique set with no duplicates
numbers = [1, 1, 2, 3, 4, 4, 5]
uniques = set(numbers)  # remove duplicates in numbers list to set
print(uniques)  # {1, 2, 3, 4, 5}

# creating new set

setA = {"Jan", "Feb", "Mar", "April", "May", "Thur"}
setB = set(["Mon", "Tue", "Wed", "Thur"])
setC = {11, 22, 33, 44, 55, 66, 77}

print(setA)
print(setB)
print(setC)

# Accessing values of a set

for x in setA:
    print(x)  # prints all set A elements

# adding elements
setB.add("Sat")
print(setB)

# # Remove elements
setB.discard("Mon")
print(setB)

# # set union
setD = setA | setB
print(setD)

# # Set intersection
setE = setA & setB
print(setE)

# set Difference
setF = {"Mon", "Tue", "wed", "Thur"}
setG = {"Sat", "Thur", "Sun", "Jan", "Feb"}

setDiff = setF - setG
print(setDiff)

# Set comparison
setF = {"Mon", "Tue", "wed", "Thur"}
setG = {"Mon", "Tue", "wed", "Sat", "Thur", "Sun", "Jan", "Feb"}

superset = setG >= setF
subset = setF <= setG

print(superset)  # True
print(subset)  # True
