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
