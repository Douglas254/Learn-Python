# generator expression used when dealing with the large data set since it takes less memory
from sys import getsizeof

values = (x * 2 for x in range(100000))  # generator object
print("gen:", getsizeof(values))  # gen: 120  bytes of memory


values = [x*2 for x in range(100000)]
# list 824464 takes large memory size as compared to generator object
print("list", getsizeof(values))
