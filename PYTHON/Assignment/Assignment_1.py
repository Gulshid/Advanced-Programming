# Password Storage and Management System
Upper_Case_letters = ['A' , 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

Lower_Case_letters = ['a' , 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Create a Database of list

database = []

print("*** Password Manager ***\n")
print("1. Add Username and Password")
print("2. Display All Username and Password")
print("3. Exit")


while True:
    choice = input("Enter the Following Option :)")
    
    if choice == '1':
        username = input("Enter Your Username :")
        password = input("Enter Your Password :")
        
        pass_parts = password.split('-')
        
        upperCase = 0
        lowerCase = 0
        
        for part in pass_parts:
            if part in Upper_Case_letters:
                upperCase += 1
            elif part in Lower_Case_letters:
                lowerCase +=1
        
        if upperCase == 2 and lowerCase == 4:
            entry = username + ":" + password
            database.append(entry)
            print("USername and Password is Successfully Added --->")
        else:
            print("Invalid Password")
            print(f"UpperCase letters : {upperCase}")
            print(f"LowerCase letters : {lowerCase}")
            print("Becasue of Password must be 2 UpperCase and 4 LowerCase Letters --->")
            
            
    elif choice == '2':
        if len(database) == 0:
            print("There is No Record of Student in Database :)")
        else:
            print("*** ALL USers ***")
            for entry in database:
                parts = entry.split(':')   
                print("USername :", parts[0])
                print("Password :", parts[1])
                print("-- --- --- --")             
            
    elif choice == '3':
        print("Good Bye ")
        break
    else:
        print("Invalid Input for Option 1, 2, 3 Exist ")
