
x = 12
y = 10

z = y
y = x
x = z
print("X:", x)
print("Y:", y)

# easiest way to use tuple packing and unpacking to swap variables
x = 12
y = 10

x, y = y, x
print("X:", x)
print("Y:", y)
