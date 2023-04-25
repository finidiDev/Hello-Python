# Functions

# Function definition
def my_function():
    print("Hello")
    print("World")

# Function call
my_function()

# Function definition
def my_function(name):
    print("Hello")
    print(name)

# Function call
my_function("World")

# Function definition
def sum_two_numbers(first_value, second_value):
    return first_value + second_value

# Function call
result = sum_two_numbers(2, 3)
print(result)

# Function definition
def print_name(name,surname):
    print(f"{name} {surname}")

# Function call
print_name(surname="John",name= "Doe")
print_name("John","Doe")

# Function definition
def print_name(name,surname="Doe"):
    print(f"{name} {surname}")

# Function call
print_name("John")

# Function definition
def print_texts(*texts):
    for text in texts:
        print(text)

# Function call
print_texts("Hello","World")
print_texts(1,(2,2),"!")
