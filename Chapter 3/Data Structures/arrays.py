
#  Arrays structure

from array import array

# arrayVarName = array('TypeCode', ['value-initializers'])

# Create and print elements of an array
array1 = array('i', [11, 22, 33, 44, 55, 66, 77, 88, 99])

for i in array1:  # traversing through an array
    print(i)

# access elements

print(array1[0])  # 11

# Add new elements
array1.insert(0, 10)
print(array1)

# remove elements

array1.remove(33)
print(array1)

# search an element
print(array1.index(44))

# update elements

array1[1] = 555

print(array1)
