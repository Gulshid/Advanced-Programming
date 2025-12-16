# greet 
def greet():
    print("Hello WOrld ! Welcome Back ...")


greet()

# greetperson
def greetperson(name):
    print(f"Name : {name}")
    

greetperson("Gulshid zada")
greetperson("Muhammad")

# person ==> name, age , city
def introduce(name, age, city):
    print(f"Name : {name},  Age : {age},    City : {city}")
    
introduce("Gulshid Zada", 23, "Peshawar")

# use return
def add(x,y):
    z = x + y
    return z

print(add(3,4))

# multiple return
def calculate(x,y):
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
    return add, sub, mul, div

print(calculate(3,4))

# Default paramter
def person( roll, name = "Gulshid ", age = 23,):
    print(f"Name :{name},  age = {age},   roll no :{roll}")
    
    
person(391)

# Calculator
def Calculator():
    # add
    def add(a, b):
        return a + b
    # sub
    def sub(a, b):
        return a - b
    # mul
    def mul(a, b):
        return a * b
    # div
    def div(a, b):
        if b != 0:
            return a / b
        else:
            return "Error"
    return add, sub, mul, div

add, sub, mul, div = Calculator()
print("Add ", add(2,3))
print("sub ", sub(2,3))
print("mul ", mul(2,3))
print("div ", div(2,3))


# function with docstring
def calculate_area(length, width):
    '''
    Parameters:
    length (float): The length of the rectangle
    width (float): The width of the rectangle

    Returns:
    float: The area of the rectangleadd, sub, mul, div = Calculator()
    
    
    '''
    
    area = length * width
    return area


print("Area :", calculate_area(3,4))
print("DOc",calculate_area.__doc__)







