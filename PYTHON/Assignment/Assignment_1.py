# Password Storage and Management System

# 1.Upper and Lower Case Letters
upper_case_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_case_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 2.Declare a Database
database = []

# 3. while True
while True:
    # Input from User at Runtime for Choices
    print("*** Password Manager ***")
    print("1. Add username and password")
    print("2. Display all usernames and passwords")
    print("3. Exit")
    
    choice = input("Enter the Following Option to Choose :")

    if choice == '1':
        username = input("Enter Your Username :")
        password = input("Enter Your Password :")
        
        pass_parts = password.split('-')
        
        upperCase = 0
        lowerCase = 0
        
        for part in pass_parts:
            if part in upper_case_letters:
                upperCase +=1
            elif part in lower_case_letters:
                lowerCase +=1
        
        if upperCase == 2 and lowerCase == 4:
            entry = username + ":" + password
            database.append(entry)
            print("Username and Password added Successfully ---->")
        else:
            print("Invalid Password")
            print("Upper Case Letter is :", upperCase)
            print("Lower Case Letter is :", lowerCase)
            print("Because Password Must have 2 Upper Case Letters and 4 Lower Case Letters")
            
    elif choice == '2':
        if len(database) == 0:
            print("There is no Record of any Person")
        else:
            print("*** All Users ***")    
            for entry in database:
                parts = entry.split(":")
                print("Username :",parts[0])
                print("Password :",parts[1]) 
                print("- - -")
    elif choice == '3':
        
        print("Good Bye")
        break
    else:
        print("Invalid Input ! Please try Again")
        
