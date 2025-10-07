# 1st program
def greet():
    print("Hello World")


# calling the function
greet()

# 2nd program
def greet_person(person):
    print(f"Hello : {person}")

# calling the function
greet_person("Gulshid")


# 3rd program
def introduce(name, age, city):
    print(f"{name} : {age} :{city}")

# calling the function
introduce("Gulshid Zada", 22, "Peshawar")


# 4th Function with Return Value
def add_number(a,b):
    result = a+b
    return result
# calling the function
sum = add_number(2,3)
print(f"The sumof two value is :{sum}")
print(f"The sum of two value is :{add_number(3,6)}")



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

# 6th  Function with Default Parameters

    



