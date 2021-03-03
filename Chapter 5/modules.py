# Modules
# Modules refer to a file containing Python statements and definitions.
# A file containing Python code, for example: example.py, is called a module, and its module name would be example.
# We use modules to break down large programs into small manageable and organized files. Furthermore, modules provide reusability of code.
# We can define our most used functions in a module and import it, instead of copying their definitions into different programs.

# # Method 1
import sys
from sales_module import cal_shipping, cal_tax

cal_shipping()  # call_shipping method get called
cal_tax()  # cal_tax method get called

# # Method 2
# import sales_module
# sales_module.cal_shipping()
# sales_module.cal_tax()


# Module search path
# import sys
print(sys.path)
