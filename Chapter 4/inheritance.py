
# Animal: Parent,Base class
class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 2

    def eat(self):
        print("eat")


# Mammal: Child,Sub class
class Mammal(Animal):
    def __init__(self):
        print("Mammal Constructor")
        self.weight = 5
        super().__init__()  # calling constructor of the Animal

    def walk(self):
        print("Walk")


# Fish: Child,Sub class
class Fish(Animal):
    def swim(self):
        print("Swim")


m = Mammal()
m.walk()
m.eat()
print(m.age)  # 2
print(m.weight)  # 5
s = Fish()
s.swim()
s.eat()
print(s.age)

# Object class - classes by default inherits from the object(Animal class) same as class attribute defined
print(isinstance(m, Mammal))  # True
print(issubclass(Mammal, Animal))  # True
print(isinstance(m, object))  # True
print(issubclass(object, Animal))  # False

# Method overriding this is the replacing or extending a method defined in the Base class


# Multi-Level inheritance
