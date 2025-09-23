print('************Ascending*****************')   
for ascen in range(0, 10):
    print('Ascending :', ascen)
    
print('************Decending*****************')   
for decen in range(10, 0, -1):
    print("Decwnding:", decen)
    
print('*************Even number****************')   

for even in range(0, 21):
    if(even%2==0):
        print("Even :" , even)
        
print('*************Odd number****************')   
for odd in range(1, 21):
    if(odd % 2==1):
        print("Odd :", odd)
        
print('*************Multiplication Table****************')   
a =int(input('Enter any number of table that you want:'))
for table in range(1, 11):
    print(f"{a} X {table} = {a * table}")
    

print("Pattern 1: Increasing numbers")
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print()  


print("Pattern 2: Decreasing numbers")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


print('*************Sum of number****************')   
total=0
for num in range(-1, 101):
    total+=num
    if(num<=5):
      print("The Num :", num)

print("total :", total)

print("*****OR****************")
sum=0
for i in range(1, 10):
    sum=sum+i
    print(f'{sum},')
    
print(f'Sum is :{sum}')

print('*************Sum of Even Number****************')  
sum_even=0
for add in range(1,21):
    if(add % 2==0):
        sum_even=sum_even+add
        print(f'Sum of Even :{sum_even}')
print(f"The Total sum of Even :{sum_even}")


print('*************Sum of Odd Number****************')  
sum_odd=0
for add in range(0,21):
    if(add % 2==1):
        sum_odd=sum_odd+add
        print(f"Sum of Odd :{sum_odd}")
print("Total sum of odd is :", sum_odd)


print('*************Skipping Number****************')  
for u in range(1, 21):
    if(u ==5 or u== 10 or u==15 or u==20):
        print("Skipping number:", u)
        continue

    print("Number is ", u)

