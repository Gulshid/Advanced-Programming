# 1st program
def greet():
    print("Hello World")


# calling the function
greet()
print("*****************")
# 2nd program
def greet_person(person):
    print(f"Hello : {person}")

# calling the function
greet_person("Gulshid")
print("*****************")

# 3rd program
def introduce(name, age, city):
    print(f"{name} : {age} :{city}")

# calling the function
introduce("Gulshid Zada", 22, "Peshawar")

print("*****************")
# 4th Function with Return Value
def add_number(a,b):
    result = a+b
    return result
# calling the function
sum = add_number(2,3)
print(f"The sumof two value is :{sum}")
print(f"The sum of two value is :{add_number(3,6)}")

print("*****************")

# 5th calculate two value 
def calculate(x,y):
    add = x+y
    sub = x-y
    div = x/y
    mul = x*y
    return add, sub, div, mul

calculate_result = calculate(2,4)
add, sub, div, mul = calculate(2,6)
print(f"The addition of two value {add}")
print(f"The subtraction of two value :{sub}")
print(f"The div of two value is :{div}")
print(f"The Mul of two value is :{mul}")
print(f'calculate result : {calculate_result}')
print("*****************")
# 6th  Function with Default Parameters
def create_greeting(name, greeting="Hello", punctuation="!"):   
    return f"{greeting}, {name}{punctuation}"

print(create_greeting("Alice")) 
print(create_greeting("Bob", "Hi")) 
print(create_greeting("Charlie", "Hey", "!!!"))
print("*****************")
# 7th Function with Keyword Arguments
def describe_pet(pet_name, animal_type = "dog", age = 1):
    print(f"i have {animal_type} named {pet_name} who is  {age} Year old ")


describe_pet("whister", "Cat", 3)
describe_pet("hamster", "nibble", 1)
describe_pet("whister", "Cat", 2)
describe_pet("whister", "Cat", 1)
describe_pet("Buddy") # use defalt value for argument
print("*****************")
# 8th. Practical Example: Calculator Functions
def Calculator():
    # add function
    def add(x,y):
        return x + y
    
    # Sub functionn
    def sub(x,y):
        return x - y
    
    # Mul function
    def mul(x,y):
        return x * y
    
    # divide function
    def div(x,y):
        if(y == 0):
            return "Error : Division by Zero"
        return x / y
    num_1 = 20
    num_2 = 5
    print(f"The additon of two value {num_1} and {num_2} is : {add(num_1, num_2)}")
    print(f"The Subtraction of two value {num_1} and {num_2} is : {sub(num_1, num_2)}")
    print(f"The Multiplication of two value {num_1} and {num_2} is : {mul(num_1, num_2)}")
    print(f"The Division of two value {num_1} and {num_2} is : {div(num_1, num_2)}")



# call the function
Calculator()

# 9th. Function with Docstring
def calculate_area(length, width):
    return length * width


result= calculate_area(2,5)
print(f"The Area of rectangle is : {result}")

    
print(calculate_area.__doc__)


