# continue Statement

# for number in range(0, 21):
#     if(number % 2 == 0):
#         continue
#     print(number)


# a = 0
# while a <= 10:
#     if a % 2 == 0:   
#         a += 1      
#         continue     
#     print(a)        
#     a += 1   

            # start, stop, condition
while True:
    table= int(input("Enter the table that you want:"))

    # for y in range(1, 11):
    #     print(f"{table} X {y} = {table * y}")

    val = 1
    while val <= 10:       
        print(f"{table} X {val} = {table * val}")
        val=val+1
    a = input('Yes/no : ').strip().lower()
    if(a  == 'no'):
        print("Program ended")
        break
        
        
        
        
   
        
    
    
    

