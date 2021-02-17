# Class: is a blue print for creating new object i.e class - Human
# Object: instance of a class i.e object - douglas,Basil,Njogu,Harrison
# class uses Pascal naming convention "FirtWordAlwaysCapital"

class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
# check if point object is an instance of Point class
print(isinstance(point, Point))


# Class parameters
class Points:
    def draw(self):
        print("draw")

    def plot(self):
        print("plot")


# you can create different objects from same class
point1 = Points()
point1.x = 5
point1.y = 8
point1.z = 9
print(point1.z)

point2 = Points()
point2.x = 2
point2.y = 4
point2.z = 6
print(point2.x)


class ComputeEngine:
    def cloud(self):
        print("Welcome to Google Cloud")

    def vm_instance(self):
        print("Create VM instance")


# object of type Compute Engine and store in a variable name
cloud_vm = ComputeEngine()
cloud_vm.cloud()  # calls the cloud method on the cloud method
cloud_vm.vm_instance()  # calls the vm instance method on the vm function
