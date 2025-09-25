import random

random_value=random.randint(1,100)
guess=0
tries=0

while guess != random_value:
    try:
        guess=int(input('Enter the Guessing nunber :'))
        tries=tries+1
        
        if guess > random_value:
            print( "The guess number is greater value")
            print('Try Again')
        
        elif guess < random_value:
            print("The guess number is less value")
            print("try Again")
        
        elif guess == random_value:
            print(f"Congrats ! You Guessed the Correct Value in {tries} tries")
    except ValueError:
        print('Please Enter an valid Number:')
        
        
        
        # Application 2: Password strength checker
# print(&quot;\n2. PASSWORD STRENGTH CHECKER&quot;)
# password = input(&quot;Enter a password to check: &quot;)
# has_upper = False
# has_lower = False
# has_digit = False
# has_special = False

# for char in password:
# if char.isupper():
# has_upper = True
# elif char.islower():
# has_lower = True
# elif char.isdigit():
# has_digit = True
# elif char in &quot;!@#$%^&amp;*&quot;:
# has_special = True

# strength = 0
# if has_upper: strength += 1
# if has_lower: strength += 1
# if has_digit: strength += 1
# if has_special: strength += 1
# if len(password) &gt;= 8: strength += 1

# print(f&quot;Password strength: {strength}/5&quot;)

# # Application 3: Shopping cart total
# print(&quot;\n3. SHOPPING CART CALCULATOR&quot;)
# items = []
# while True:
# item_name = input(&quot;Enter item name (or &#39;done&#39; to finish): &quot;)
# if item_name.lower() == &#39;done&#39;:
# break

# try:
# item_price = float(input(&quot;Enter item price: $&quot;))
# item_quantity = int(input(&quot;Enter quantity: &quot;))
# items.append((item_name, item_price, item_quantity))
# except ValueError:
# print(&quot;Invalid input! Please enter numbers for price and quantity.&quot;)
# continue

# total = 0
# print(&quot;\nRECEIPT:&quot;)
# print(&quot;-&quot; * 30)
# for name, price, quantity in items:
# item_total = price * quantity
# total += item_total
# print(f&quot;{name} × {quantity}: ${item_total:.2f}&quot;)

# print(&quot;-&quot; * 30)
# print(f&quot;TOTAL: ${total:.2f}&quot;)

# # Run practical applications
# practical_applications()

# # Main program execution
# if __name__ == &quot;__main__&quot;:
# print(&quot;LOOPS COMPLETE DEMONSTRATION&quot;)
# print(&quot;=&quot; * 60)

# # Run all demonstration programs
# basic_for_loop()
# while_loop_demo()
# control_statements()
# range_function_demo()
# practical_applications()

# print(&quot;\n&quot; + &quot;=&quot; * 60)
# print(&quot;ALL DEMONSTRATIONS COMPLETED!&quot;)
# print(&quot;=&quot; * 60)