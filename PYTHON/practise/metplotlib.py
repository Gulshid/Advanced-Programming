import matplotlib.pyplot as plt
# # program 1
x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.plot(x,y)
plt.title("SImple line Plot")
plt.xlabel("X values")
plt.ylabel("y values")
plt.show()

# program 2
x = [1,2,3,4]
y = [10,20,15,25]
plt.plot(x, y, color="red", linestyle='-', marker='o')
plt.title('stylelinegraph')
plt.show()


# # # program 3
student = ['ALi', 'sara', 'umar', 'hamza']
marks = [88,92,85,78]
plt.bar(student, marks)
plt.title("student marks ")
plt.xlabel("student")
plt.ylabel("marks")
plt.show()

# program 4
country = ["Pak", "India", "chaina", "iran"]
papulation = [230, 1400, 1440, 85]

plt.barh(country, papulation)
plt.title("Country Papulation")
plt.show()

# program 5
x = [5, 7, 8, 9, 4]
y = [10, 12, 15, 20, 5]

plt.scatter(x,y)
plt.title("Scatter plot Example")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# program 6
ages = [34,22,23,54,21,50,43,23,22,26]
plt.hist(ages, bins= 5)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# program 7
labels = [ "window", "ANdroid", "IOs", "other"]
shares = [70,20,5,5]
plt.pie(shares, labels = labels, autopct = "%1.1f%%")
plt.title("MObile OS market share ")
plt.show()


# program 8
year = [2018, 2019, 2020, 2021,2022]
sales_A = [50, 60, 65, 70, 80]
sales_B = [40, 55, 60, 68, 75]

plt.plot(year, sales_A, label="Product A")
plt.plot(year, sales_B, label="Product B")
plt.title("Sales Comparison ")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()

# program 9
x = [1, 2, 3, 4]
y = [2, 5, 8, 10]
plt.plot(x,y)
plt.grid(True)

plt.title("Graph with Grid")
plt.show()

# program 10
x = [1, 2, 3, 4]
y1 = [2, 3, 4, 5]
y2 = [5, 4, 3, 2]
plt.subplot(1,2,1)
plt.plot(x,y1)
plt.title("Increasing ")

plt.subplot(1,2,1)
plt.plot(x,y2)
plt.title("Decreasing ")

plt.show()
