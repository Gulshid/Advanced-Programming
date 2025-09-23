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
    
    
for i in range(1, 6): 
  for j in range(1, i + 1):
    print(j, end =" ")
    print()


    
    