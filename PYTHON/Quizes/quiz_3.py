# 1st --> find the odd and even number from nterm

a=0
value=0

while True:
    try:
        a = int(input("Enter a number (Even / Odd): "))
        
        if a % 2 == 0:
            print(f"The number {a} is Even")
        else:
            print(f"The number {a} is Odd")
        
        value = input("Do you want to enter another number? (Yes/No): ").strip().lower()
        
        if value == "no":
            print("Program ended.")
            break
    
    except ValueError:
        print("Please enter a valid number.")


# 2nd ---> find factorial of any number
#def fact(numb):
 #   if ( numb == 1 or numb == 0):
      #  return 1
  #  else:
  #      return numb * fact(numb - 1)


#a= int(input('Enter the number for fact:'))
#print(f"The  factorial of {a} is :{fact(a)}")

# or 
number = int(input("Enter the number to find the factorial:"))

fact = 1

for j in range(1, number + 1):
    fact=fact*j

print(f"The factorial of {number} is {fact}")




# 3 ---> find the prime number of any number 
# 2,3,5,7,11,13,17,19
#. only divisable by 1 or itself
num = int(input("Enter a number: "))
is_prime = True  

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a Prime number")
else:
    print(f"{num} is NOT a Prime number")






        
    
    