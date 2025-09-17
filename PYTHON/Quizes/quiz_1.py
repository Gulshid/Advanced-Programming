# problem 1 : find the ticket price according to age , time and day
age=int(input("Enter Your age:"))
time =int(input("Enter the movie time :"))
day=input('Enter the day :').strip().lower()

if(age <13):
    price=8
elif age>=13 or  age == 64:
    price=12
elif age >=65:
    price=10

if(time<17):
    price=price-2

if (day == 'wednesday'):
    price=price-3
    
print(f' Final Ticket price :{price}')



# Problem 2: Loan Eligibility Checker

age = int(input("Enter your age: "))
income = float(input("Enter your annual income: "))
credit_score = int(input("Enter your credit score: "))

if 21 <= age <= 65 and income >= 30000 and credit_score >= 650:
    print("Eligible for loan.")
    if credit_score > 750 and income > 50000:
        print("You qualify for a premium rate loan.")
    else:
        print("You qualify for a standard rate loan.")
else:
    print("Not eligible for loan.")

# Problem 3: Weather Advisory System

temp = float(input("Enter the temperature (°C): "))
rain = input("Is it raining? (yes/no): ").strip().lower()
wind_speed = float(input("Enter wind speed (km/h): "))

# Base message based on temperature
if temp < 0:
    message = "Extreme cold warning"
elif 0 <= temp <= 10:
    message = "Cold weather"
elif 11 <= temp <= 25:
    message = "Pleasant weather"
else:
    message = "Warm weather"

# Add rain condition
if rain == "yes":
    message += " - Bring umbrella"

# Add wind condition
if wind_speed > 30:
    message += " - Windy conditions"

print("Weather Advisory:", message)




# Problem 4: Shopping Discount Calculator

membership = input("Enter membership level (gold/silver/bronze/none): ").strip().lower()
purchase = float(input("Enter purchase amount: "))

# Base discount by membership
if membership == "gold":
    discount = 0.20
elif membership == "silver":
    discount = 0.15
elif membership == "bronze":
    discount = 0.10
else:
    discount = 0.0
    if purchase > 100:  # 5% discount for none
        discount = 0.05

# Additional 5% for purchases > $200
if purchase > 200:
    discount += 0.05

final_price = purchase - (purchase * discount)

print(f"Final price after discounts: ${final_price:.2f}")



    