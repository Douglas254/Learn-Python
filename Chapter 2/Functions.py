def greet():  # define a function using "def"
    print("Hi, there")
    print("Welcome aboard")


greet()  # Calling a function

# Arguments


# Parameter - is the input that you define for your function
def greetings(first_name, Last_name):
    print(f"Hi {first_name} {Last_name}")
    print("Welcome Aboard")


# Arguments - is the actual value for a given parameter
greetings("Douglas", "Obara")
greetings("Basil", "Friend")

# Types of functions
# 1.perform  a task


def Github(name):
    print(f"Hi, {name}")


Github("Douglas254")

# 2.calculate and return a value


def get_name(name):
    return "..."


print(get_name("douglas"))


# keyword argument
def increment(number, by):
    return number + by


print(increment(2, by=1))  # by=1 is the keyword argument


# Default argument
def incremnt(number, by=1):  # by=1 is the Default argument
    return number + by


print(incremnt(2))


# *args - * arguments
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))


# **args - ** arguments
def save_user(**user):
    # you can use [""] to access each keyword argument e.g print(user["name"])
    print(user)


save_user(id=1, name="Douglas", age=23)


# Scope -  Global and Local variable
message = "a"  # global variable


def greet_variable(name):
    global message  # making message variable globally using global keyword
    message = "b"  # Local variable
    return name


print(greet_variable("Hello"))
print(message)
