
# EXCEPTIONS:
# This are used to manage errors and avoid system crash by handling error occurance
# Exit Code of 0-->Success no error and Exit code 1-->Error/program crash
# Try Except is used to catch this errors

id_number = int(input("Enter your id number: "))
# Returns valueError incase a user enters value that's not an integer
print(id_number)

try:
    id_number = int(input("Enter id: "))
    salary = 20000
    savings = salary/id_number
    print(id_number)
except ZeroDivisionError:
    print("Id number cannot be Zero")
except ValueError:
    print("Not a valid input, try again ! ")


# COMMENTS
"Hash tag used for commenting out code or explanation"
"""----multiple line comment--"""


try:
    age = int(input("Enter age"))
    xfactor = 10 / age
except ValueError:
    print("Please enter a valid age")
except ZeroDivisionError:
    print("Age cannot be zero")
else:
    print("No exceptions were thrown in the process")
