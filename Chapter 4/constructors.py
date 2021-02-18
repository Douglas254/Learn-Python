# class functions that begin with double underscore __ are called special functions
#  as they have special meaning.
# __init__(): this special function gets called whenever a new object of that class is
#  instantiated,this type of function is also called constructors in OOP

class Point:
    # creating constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"point({self.x},{self.y})")


point = Point(2, 3)
point.draw()


# Classes vs Instance Attributes
# class attributes are shared across all instances of a class
# instance attributes are attributes that belong to the Point instances or the point object

class Points:
    default_color = "Red"  # class attribute

    def __init__(self, x, y):
        self.x = x  # instance attribute
        self.y = y  # instance attribute

    def draw(self):
        print(f"point({self.x},{self.y},{self.z})")


# change default color of point object to green across all instances
Points.default_color = "Green"

point = Points(1, 2)
point.z = 5  # instance attribute
point.draw()
print(point.default_color)  # point object to get access to this attribute
print(Points.default_color)  # Points class to get access

another = Points(6, 8)
another.z = 9
another.draw()
print(another.default_color)


# class vs instance method
class Point2:
    # creating constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # creating method
    @classmethod  # decorator is a way to extend the behaviour of a method or function
    def Zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"point({self.x},{self.y})")


point = Point2.Zero()
point.draw()


# chalenge 1
# create a new type person,has name attribute and talk method

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("I'm talking")


person = Person("Douglas254")
person.talk()
print(person.name)


# Challenge 2
# create a new animal class, with two methods, legs and eating, and concatenate variables

class Animal:
    def __init__(self, name_, leg, food):
        self.name_ = name_
        self.leg = leg
        self.food = food

    def name(self):
        print("")

    def eating(self):
        print(f"Hello i am {self.name_} and i like eating {self.food}")

    def legs(self):
        print(f"i have {self.leg} legs")


dog = Animal("Dog", 4, "Meat")
dog.eating()
dog.legs()

cow = Animal("Cow", 4, "Grass")
cow.eating()
cow.legs()
