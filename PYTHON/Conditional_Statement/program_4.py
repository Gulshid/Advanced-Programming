# Example 1: list of number
print("*****Example of list of number *******")
number=[1,2,3,4,5,6]
for num in number:
    print(num)
    
print("*****Example of list of fruite *******")
# Example 2: list of fruite
fruite= ["Apple", "Banana", "Orange", "Cherry"]
for fruit in range(len(fruite)):
    print(fruite[fruit])

print("*****Example of list of number to add 3 to each Number*******")
# Example 3: Modifying list elements
score=[85, 92, 78, 95] 
for i in range(len(score)):
    score[i]=score[i] + 3
    print(score[i])   
print("****** WHILE LOOP WITH LIST ***********")
# Example 4: While loop with list
colors= ["Green", "Blue", "Red", "White", "yellow"]
i=0
while(i<len(colors)):
    print(f"{colors[i]}")
    i+=1
    
# Example 5: find the factorial of any number using loop
num = int(input("Enter the value for fact:"))
fact = 1
if(num < 1):
    print("There is no calculation for Negative Numbers")
elif (num == 0 or num == 1):
    print(f'The fact of {num} is 1')
else:
    for i in range(1, num + 1):
        fact = fact * i
    print(f'the factorial of {num} is {fact}')
    
# Example 6: find the factorial of any number using while loop
a = int(input("Enter the value for fact:"))
factorial = 1  # initial value is 1
if(a == 0 or a == 1):
    print(f"The factorial of {a} is 1")
elif (a < 0):
    print(f'There is no factorial for Negative Number')
else:
    b = 1
    while(b<=a):
        factorial = factorial * b
        b=b+1
    print(f"The factorial of {a} is {factorial}")


# Example 7: find the factorial for 1 to 10
for k in range(1, 11):
    fact = 1
    for s in range(1, k + 1):
        fact = fact * s
    print(f"{k}! \t factorial \t {fact}")

# Example 8: Find the fibonacci Series 
num =int(input("Enter the term of value that can fibonacci series Want :"))
first_term = 0
second_term = 1
if(num >=1):
    print(first_term , end = " ")
if(num >=2):
    print(second_term , end = " ")

for i in range(1, num + 1):
    next = first_term + second_term
    print(next , end= " ")
    first_term = second_term
    second_term = next 
print()

# Example 9: find the prime number 
# 2,3,5,7,11,13,17,19
#. only divisable by 1 or itself
# If we enter 11
# it check and 11 divide from 2 ---- 10  if anyone divide completely so the number is prime number 
num = int (input("Enter the Number for Prime Number:"))
Is_Prime= True

if(num <= 1):
    # 1,0 and Negative value has no Prime Number we start with 2
    Is_Prime=False
else:
    for o in range(2, num):
        if(num % o == 0):
            Is_Prime = False
            break


if(Is_Prime):
    print(f"{num} is a prime Number")
else:
    print(f"{num} is not a prime Number")
