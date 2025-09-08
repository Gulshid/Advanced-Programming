# Simple greeting program
name=input("What's your Name:")
age=int(input("What's your Age:"))
print(f' My Name is : {name} and my Age is : {age}')
print(f'Next year {name} you will be ', age+1, "year old\n")


# Working with different data types
favorite_color='blue'
heigth=5.10
is_student=True
print(name + "'s Favorite Color is :", favorite_color)
print(f"They are {heigth:.2f} feet tall")
print(f"Are they a student? {is_student}")


# Define variables
name="Alice"
age=25
city='New York'
Score=95.5
is_student=True
print(name, age, city, Score, is_student)

# Define variables
name='Bob'
age=30
profession='Engineer'
print("Name "+name + ",Age "+ str(age) + ",Profession "+ profession)


#Define variables
product='Laptop'
price=999.99
quantity=2
total= price * quantity
print(f"Product {product} , proce {price} , quantity {quantity}, Total {total}")


# Define variables
name='Charlie'
grade= 'A'
persentage=90.5
print("name {}, grade {}, persentage {}%".format(name, grade, persentage))

# Define variables
temperature=72.5
humidity=65
weather='sunny'
print(f"Temperature {temperature}°F,  Humidity {humidity}% ,Condition {weather}")

#Define variables
title='Python Programming'
author='john Smith'
page=350
price=49.99
print(f''' 
        Book Details:
        ============
        Title:{title}
        Author: {author}
        Page: {page}
        Price: ${price}           
    ''')


# 1. Converting to Integer (int())
print("=======CONVERTING INTEGER=========")
# From float to int (truncates decimal part)
price=19.99
price_int=int(price)
print(f'Price of float {price} and Price of Int is {price_int}')


# From string to int (if string represents a whole number)
number_str='42'
number_int=int(number_str)
print(f' String  {number_str}  to Integer :{number_int}')

# From boolean to int
true_value=int(True)
false_value=int(False)
print("True Integer value is :", true_value)
print("False Integer value is :", false_value)


# 2. Converting to Float (float())
print("=======CONVERTING TO FLOAT=========")
# From int to float
age=25
age_float=float(age)
print(f"Integer  :{age} to Float : {age_float}")

# From string to float
pi_str='3.1415'
pi_float=float(pi_str)
print(f'String {pi_str} to FLoat : {pi_float:.4f}')

# From boolean to float
true_value=float(True)
false_value=float(False)
print(f"The true value is :{true_value}")
print(f"The false value is : {false_value}")

# From Int to String
count=100
str_count=str(count)
print(f'The Integer {count} to String {str_count}')

# From float to string
temperature=98.6
str_temperature=str(temperature)
print(f' Float {temperature} to String {str_temperature}')

# From boolean to string
true_str=str(True)
false_str=str(False)
print("The True value of Boolean to String is : ", true_str) 
print("The False value of Boolean to String is : ", false_str) 

# From list to string
fruite =['apple', 'banana', 'cherry']
fruite_str=str(fruite)
print(f'List {fruite} to String {fruite_str}')


# 4. Converting to Boolean (bool())
print("=======CONVERTING TO BOOLEAN=========")
# From int to boolean (0 = False, any other number = True)
ZERO_bool=bool(0)
Five_bool=bool(5)
ten_bool=bool(10)

print(f" Integer 0 To Boolean: {ZERO_bool}")
print(f" Integer 5 To Boolean: {Five_bool}")
print(f" Integer 10 To Boolean: {ten_bool}")

# From float to boolean
zero_float_bool=bool(0.0)
pi_bool=bool(3.14)
print(f' False Float to Boolean :{zero_float_bool}')
print(f' True Float  to Boolean:{pi_bool}')


# From string to boolean (empty string = False, any other string = True)
empty_str_bool=bool('')
hello_str_bool=bool('hello')
print(f'empty String to Boolean :{empty_str_bool} ')
print(f'non_empty String to Boolean :{hello_str_bool} ')

# From list to boolean (empty list = False, non-empty list = True)
empty_list_bool=bool([])
full_list_bool=bool([1,2,3])
print(f'Empty List to Boolean :{empty_list_bool}')
print(f'Non-Empty List to Boolean :{full_list_bool}')






