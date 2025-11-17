# a= 9
# b=4
# c="hello"
# print(f'''
#       a :{a},
#       b: {b},
#       c: {c}


# ''')

# floating = 4.344
# integer= int(floating)
# print(f"float :{floating:.2f}   , int :{integer}") 

# a = False
# b = int(a)
# print(f"a : {a} , b: {b}")


# a = 24
# b = float(a)
# print(f'a : {a} , b: {b}') 

# a = "34"
# b = float(a)
# print(f'a : {a} , b: {b}') 


# a = False
# b = float(a)
# print(f'a : {a} , b: {b}') 

# a = 23
# b = str(a)
# print(f"a : {a}. , b : {b}")

# a = 23.34
# b = str(a)
# print(f"a : {a}. , b : {b}")

# a = True
# b= str(a)
# print(f"a : {a}. , b : {b}") 

# a =[1,2,3]
# b = str(a)
# print(f"a : {a}. , b : {b}") 

# a = 3
# b = bool(a)
# print(f"a : {a}. , b : {b}") 

# a = 0.00
# b = bool(a)
# print(f"a : {a}. , b : {b}") 


# a = ""
# b = bool(a)
# print(f"a : {a}. , b : {b}") 

# a = []
# b = bool(a)
# print(f"a : {a}. , b : {b}") 


# a = "String "
# b = list(a)
# print(f"a : {a}. , b : {b}") 


# a = (1,2,3)
# b = list(a)
# print(f"a : {a}. , b : {b}") 

# a = range(5)
# b = list(a)
# print(f"a : {a}. , b : {b}") 



# for i in range(5):
#     print(i)
    



# Celsius = float(input("Enter the Celsius :"))
# fah = (Celsius * 9/5) +  32
# print(f" The Tempreture is Celsius :{Celsius } and fahrenheit :{fah}")


# fahre = float(input("Enter the fah :"))
# cel = (fah - 32) * 5/9

# print(f" The Tempreture is Celsius :{fahre } and fahrenheit :{cel}")


# Voting Program 
# age = int(input("Enter  Your Age:"))
# reminning_age  = 18 - age

# if age >= 18:
#     print('You Are Eligable for Voting...')
# elif age <18:
#     print("You Are Not Eligable for Voting...")
#     print(f"The Reminng Age for Voting for you is :{reminning_age}")

# Student Grading SYstem
# score = int(input("Enter Your Score : "))

# if score >= 85:
#     print("Grade A+")
# elif score >=75:
#     print("Grade A")
# elif score >=65:
#     print("Grade B")
# elif score >=55:
#     print("Grade C")
# elif score >=45:
#     print("Grade D")
# elif score >=40:
#     print("Grade E")
# else:
#     print("Grade F : You Are Failed...")


# Celsius to fahrenheit and fahrenheit to Celsius

# Celsius to Fahrenheit
# Cel = float(input("Enter Celsius:"))
# fah = (Cel * 9/5) + 32

# print(f"The Celsius of {Cel} is : {fah}")


# # Fahrenheit to Celsius
# fahren = float(input("Enter Fahrenheit :"))
# cel = (fahren - 32) * 5/9
# print(f"The Fahrenheit of {fahren}. is : {cel}")


# laon Ammount System
# age = int(input("Enter Your Age :"))
# income = int(input("Enter Your total Income / per month :"))
# credit_score = int(input("Enter Your credit Score :"))

# if age >=21:
#     if income >= 30000:
#         if credit_score >=650:
#             print("You Are Eligable for Loan Ammount...")
        
#             if income >= 50000 and credit_score >=750:
#                 loan_amount = 100000
#             elif income >= 40000 and credit_score >=700:
#                 loan_amount = 75000
#             elif income >=30000 and credit_score >=650:
#                 loan_amount = 50000
#             else:
#                 loan_amount = 25000
#             print(f"Max Loan Amount : {loan_amount}")
#         else:
#             print("credit Score too Low ")
#     else:
#         print("NOt Eligable income too low")
# else:
#     print("You are not eligable for loan amount ")


# find the tempreture ---> cold or hot 
# tempreture = float(input("Enter the Tempreture :")) 
# if tempreture >=30:
#     print("Sunny Weather tempreture")
# elif tempreture >= 20:
#     print("Normal tempreture")   
# elif tempreture >=10:
#     print("Cold Tempreture")
# elif tempreture >=0:
#     print("Very Cold Tempreture")
# else:
#     print("Very Very Cold") 


# Number check 
# Number =  int(input("Enter any Number :"))
# if Number == 1:
#     print("The value of Number is :",Number)
# elif Number == 2:
#     print("The value of Number is :",Number)
# elif Number == 3:
#     print("The value of Number is :",Number)
# elif Number == 4:
#     print("The value of Number is :",Number)
# elif Number == 5:
#     print("The value of Number is :",Number)
# elif Number == 6:
#     print("The value of Number is :",Number)
# else:
#     print("The Number neither 1,2,3,4,5,6 and it is :", Number)
    
    
# Positive and Negative Number check
# Num = int(input("Enter Any Number to check whether it is Popsitive or Negative :"))
# if Num > 0:
#     print(f"The Number {Num} is Positive Number")
# elif Num < 0 :
#     print(f"The Number {Num} is Negative Number")
# else:
#     print(f"The Number is {Num} Is Zero ")


# prime Number Check
# num = int(input('Enter the Number to check the prime :'))
# if num <=1:
#     print(f"{num} :-> There is No Prime Number for 0,1 or Negative Number ")
# else:
#     is_true = True
#     for o in range(2, num):
#         if num % o == 0:
#             is_true = False
#             break
    
#     if is_true:
#         print(f"The Number {num} is Prime Number ")
#     else:
#         print(f"The Number {num} is Not a Prime Number")


# Quiz Game , Question 5 , score 0
# print("***Welcome to Quiz***")
# print("**** Answer the following questions ? ***")
# print("1. What is the Result of : 5 == 5 and 3 > 1 ?")
# print('''
# (a) : True
# (b) : False
# (c) : Error  
# ''')

# score = 0
# answer_1 = input("Select on of these (a/b/c) :").lower()
# if answer_1 == 'a':
#     print("Correct")
#     score = score + 1
# elif answer_1 == 'b':
#     print("Incorrect ! The Correct Answer is a")
# elif answer_1 == 'c':
#     print("Incorrect ! The Correct Answer is a")
    
    



# print("2. Which Operator has the higher precedence and , Or ")
# print('''
# (a) : and
# (b) : Or 
# (c) : same  
# ''')


# answer_2 = input("Select on of these (a/b/c) :").lower()
# if answer_2 == 'a':
#     print("Correct")
#     score = score + 1
# elif answer_2 == 'b':
#     print("Incorrect ! and has higher precdenece")
# elif answer_2 == 'c':
#     print("Incorrect ! and has higher precdenece")
    



# print("3. WWhat does this code output: not(5>3) or(2 < 1) ")
# print('''
# (a) : true
# (b) : False 
# (c) : Error  
# ''')


# answer_3 = input("Select on of these (a/b/c) :").lower()
# if answer_3 == 'a':
#     print("Incorrect ! b is the correct Answer")
# elif answer_3 == 'b':
#     print("Correct")
#     score +=1
# elif answer_3 == 'c':
#     print("Incorrect ! b is the correct Answer")
    
    
    
# print("4. Which is not Relational Operator : ")
# print('''
# (a) : ==
# (b) : != 
# (c) : &&  
# ''')


# answer_4 = input("Select on of these (a/b/c) :").lower()
# if answer_4 == 'a':
#     print("Incorrect ! c is the correct Answer")
# elif answer_4 == 'b':
#     print("Incorrect ! c is the correct Answer")
# elif answer_4 == 'c':
#     print("Correct")
#     score +=1
    


# print("5. What is the result of  10 ! = 10: ")
# print('''
# (a) : True
# (b) : False 
# (c) : Error  
# ''')


# answer_5 = input("Select on of these (a/b/c) :").lower()
# if answer_5 == 'a':
#     print("Incorrect ! b is the correct Answer")
# elif answer_5 == 'b':
#     print("Correct")
#     score +=1
# elif answer_5 == 'c':
#     print("Incorrect ! b is the correct Answer")


# persentage = (score / 5) * 100
    
    



# if persentage >=90:
#     grade = 'A+'
# elif persentage >=80:
#     grade = 'A'
# elif persentage >=70:
#     grade = 'B'
# elif persentage >=60:
#     grade = 'C'
# elif persentage >=50:
#     grade = 'D'
# elif persentage >=40:
#     grade = 'E'
# elif persentage >=30:
#     grade = 'F'
# else:
#     grade = 'Failed'

        
# print("The Total Number / Score  :", score)
# print("The Persentage   :",persentage )
# print(" With grade    :",grade )
    
    
    
# Ascending in for loop 
# print("Ascending Order from 0 ---- 10")
# for p in range(0,11):
#     print(p, end=" ")

# print("\n")

# print("Descending Order from 10 ---- 0")

# for q in range(10, 0, -1):
#     print(q, end= " ")
    
# print("\n")
# Even 
# for i in range(0,21):
#     if(i % 2 == 0):
#         print(i, end= " ")

# print("\n")


# # Odd 
# for i in range(0,21):
#     if(i % 2 == 1):
#         print(i, end= " ")

# print("\n")


# Even

# for j in range(0,21, 2):
#     print(j, end= " ")
# print("\n")
# # Odd
# for j in range(1,21, 2):
#     print(j, end= " ")

# print("\n")

# table = int(input("Enter the table that you want :"))
# for i in range(0, 11):
#     print(f"{table} X {i} = {table * i}")




# sum  = 0
# for w in range(0,31):
#     sum = sum + w
#     print(sum, end = " ")
# print("\n")


# print("The Total sum from 0 to 30 :", sum)
# Skipped Number 

# for h in range(1,21):
#     if(h == 5 or h == 10 or  h == 15 or h == 20):
#         continue
#         print(h, end= " ")

#     print(h, end= " ")


# # Ascending order in while loop
# i = 0
# while i<=10:
#     print(i, end= " ")
#     i +=1


# Descending order in while loop
# i = 10
# while i>=0:
#     print(i, end= " ")
#     i -=1
# print("\n")


# Sum Number
# sum = 0
# j = 0
# while j<=10:
#     sum +=j
#     print(sum, end= " ") 
#     j+=1


# Even Number
# i  = 0
# while i <=20:
#     if(i% 2 == 0):
#         print(i, end= " ")
#     i+=1
    
    
    
# Odd Number
# i  = 0
# while i <=20:
#     if(i% 2 == 1):
#         print(i, end= " ")
#     i+=1


# table in while loop 
# table = int(input('enter the table value :'))
# i = 1
# while(i<=10):
#     print(f"{table} X {i} = {table * i}")
#     i+=1    


# Ascending and descending ---USer Control System
# start = int(input('Enter the starting point :'))
# end =  int(input('Enter the ending point :'))
# step =  int(input('Enter the step '))

# current = start

# if step > 0:
#     while current<= end:
#         print(current, end= " ")
#         current+=step
# else:
#     while current >= end:
#         print(current, end = " ")
#         current-=step

# Guessing Game
# import random

# rand = random.randint(0,10)
# attempt = 0

# while True:
#     guess = int(input('Enter the Guess Value:'))
#     attempt +=1
    
#     if guess > rand:
#         print("You Enetred very High Value , enter Low value ")
#     elif guess < rand :
#         print("You Enetred very Low  Value , enter High value ")
#     elif guess == rand:
#         print("COngrate You Guessed the correct value ")
#         break
    
#     print("Attempt :", attempt)
# print("You Guessed the value in :", attempt)

# find the factorial using loop
# fact = 1
# num = int(input('Enter the fact Num :'))

# for i in range (1, num + 1):
#     fact = fact * i
# print(f"The factorial of : {num} is {fact}")

# fact = 1
# num = int(input('Enter the fact Num :'))
# i  = 1
# while i <=num:
#     fact *= i
#     i+=1

# print(f"The factorial of {num}. is {fact}")


# num = int(input('Enter any num :'))
# if num <=1:
#     print("There is no prime number for 0 , 1 and negative value ")
# else:
#     istrue= True
#     for i in range(2, num):
#         if num % i == 0:
#             istrue = False
#             break
    
#     if istrue:
#         print("Prime number")
#     else:
#         print("Not a Prime Number")        

    
# fibanocci Series 
# first = 0
# second = 1
# num = int (input("Enter the num :"))
# if num >= 1:
#     print(first)
# if num >= 2:
#     print(second)
    
# for i in range(3,num + 1):
#     next = first + second
#     print(next)
#     first = second
#     second = next


# function 
# Prime Number fucntion
# def prime():
#     num = int(input('Enter a Number:'))
#     if(num <=1):
#         print("There is no prime number for 0 1 or negative value ")
#     else:
#         isTrue= True
#         for i in range(2, num):
#             if num % i == 0:
#                 isTrue = False
#                 break
        
#         if isTrue:
#             print('Prime Number ')
#         else:
#             print("Not a Prime Number ")
                
# prime()



# factoriall 
# def fact(num):

#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * fact(num - 1)
# n = int (input("Enter the value"))
# print(fact(n))
    
    
# fibonocci 
# def fib(n):
#     first = 0
#     second = 1

#     if n >=1:
#         print(first,end=" ")
#     if n >=2:
#         print(second, end= " ")
#     for i in range(3, n + 1):
#         next = first + second
#         print(next, end= " ")
#         first = second
#         second = next
#     print("\n")

# h = int (input("Enter the value"))
# fib(h)


# num = [1,2,3,34,5]
# for i in num :
#     print(i)


# a =['apple', 'banana', 'peach']
# for o in range(len(a)):
#     print(f"{o} {a}")
    
    
# b = [1,2,3,4,5]
# for k in range(len(b)):
#     b[k]+=6
# print(b)

# student_mxarks=int(input("Enter the student marks: "))
# if student_mxarks >=500:
#     grade = 'A+'
# elif student_mxarks >=400:
#     grade = 'A'    
# elif student_mxarks >= 300:
#     grade = 'B'
# elif student_mxarks >= 200:
#     grade = 'C'
# elif student_mxarks >=100:
#     grade = 'D'
# else:
#     grade = 'E'
# print(f"the student marls {student_mxarks} and grade {grade}")


# for i in range(1, 21, 2):
#     print(i, end= " ")
# print("\n")

# fact = 1
# num = int (input("Enter the value :"))
# for i in range(1,num+1):
#     if num == 0 or num == 1:
#         print("1")
#     elif num < 0:
#         print("There is no fact fornnragtive value ")
#     else:
#         fact = fact * i
#         print(f"The fact of {num} is {fact} ")\
    
    


# fact = 1
# num = int(input('Enter the value :'))
# if num <0:
#     print("There is no fact for negative value ")
# elif num == 0 or num == 1:
#     print(f"The fact if {num} is 1")
# else:
#     for i in range(1, num + 1):
#         fact = fact * i
#     print(f"The fact of {num} is {fact}")   


# def fact(n):
#     if n <0:
#         return "There is no fact fr negative number:"
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
    

# num = int(input('Enter the value :'))
# print(fact(num))



    
