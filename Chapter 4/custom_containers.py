
class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        # check if we have tag in the dictionary and if we don't set its value to 1 otherwise increment by 1
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        # encapsulating the case sensitivity of this class
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):  # get the length of the object
        return len(self.tags)

    def __iter__(self):  # iteration
        return iter(self.tags)


cloud = TagCloud()
cloud["python"] = 10  # get an item by its key and set to 10
len(cloud)  # get no of items in a container
cloud.add("Python")  # calling add method
cloud.add("python")
cloud.add("python")
print(cloud.tags)
for tag in cloud:  # iterate over a cloud object
    print(tag)
print(cloud["PYTHON"])


# private members
# we use double underscores to make attributes private i.e __tags
# click the attribute press f2 ,put __ and then press enter


# properties
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


product = Product(-30)
print(product.price)
