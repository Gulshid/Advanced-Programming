# ************Ascending************
print("*******Ascending*********"),
counter=1
while counter <=10:
    print('Number is :', counter)
    counter=counter+1
    
print("*******descending*********"),
counter=10
while counter>=0:
    print('Number is :', counter)
    counter-=1
    
print("*******Even Number*********"),
number=2
while number <=20:
    if(number % 2== 0):
        print('Even number :', number)
    number+=1
    
print("*******Odd  Number*********"),
number=1
while number <=21:
    if( number % 2 == 1):
        print("Odd Number :", number)
    number+=1
print("*******User Controlled  Counting*********"),
start=int(input("Enter Starting Number:"))
end=int(input("Enter the ending Number:"))
step=int(input("Enter the step size:"))

current = start
print(f"Counting form {start} to {end} with the {step} ")

if step > 0:
    while current <=end:
        print(current, end = " ")
        current+=step
else:
    while current >= end:
        print(current, end = " ")
        current+=step
        
        
