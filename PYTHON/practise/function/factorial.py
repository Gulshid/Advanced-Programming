# fact using for loop
def fact():
    n = int(input("Enter the value :"))
    if n < 0:
        print("There is no fact for nragtive num ")
        return
    else:
        factorial = 1
        for i in range(1 , n + 1):
            factorial *= i
        print(f'The fact of {n} is {factorial}')
        
fact()

# fact using while loop
def fact():
    n = int(input("Enter the value :"))
    factorial = 1
    
    i = 1
    while i <= n:
        factorial = factorial * i
        i+=1
    print(f"The factorial of {n} is {factorial}")
fact()

# factorial table 
def table_fact():
    for i in range(1, 11):
        fact = i
        for j in range(1, i + 1):
            fact *= j
        print(f"{i} \t  {fact}")
    
table_fact()

# fact using recursive
def fact(n):
    if n < 0:
        return "There is no fact for negative nubers"

    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


num = int(input("Enter the value : "))
res = fact(num)
print(f"the fact of {num} is {res}")
