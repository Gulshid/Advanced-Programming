import matplotlib.pyplot as plt
# ⭐ Program 1: Simple Line Plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()


# ⭐ Program 2: Line Plot with Style
# import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.plot(x, y, color='red', linestyle='--', marker='o')
plt.title("Styled Line Graph")

plt.show()

# ⭐ Program 3: Bar Chart
students = ["Ali", "Sara", "Umar", "Hamza"]
marks = [88, 92, 77, 85]

plt.bar(students, marks)
plt.title("Students Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()

# ⭐ Program 4: Horizontal Bar Chart
countries = ["Pakistan", "India", "China", "Iran"]
population = [230, 1400, 1440, 85]

plt.barh(countries, population)
plt.title("Country Populations")

plt.show()

# ⭐ Program 5: Scatter Plot
x = [5, 7, 8, 9, 4]
y = [10, 12, 15, 20, 5]

plt.scatter(x, y)
plt.title("Scatter Plot Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()

# ⭐ Program 6: Histogram
ages = [18, 22, 25, 30, 35, 40, 22, 25, 30, 35, 40]

plt.hist(ages, bins=5)
plt.title("Age Distribution")
plt.xlabel("Ages")
plt.ylabel("Frequency")

plt.show()

# ⭐ Program 7: Pie Chart
labels = ["Android", "iOS", "Windows", "Others"]
shares = [70, 20, 5, 5]

plt.pie(shares, labels=labels, autopct='%1.1f%%')
plt.title("Mobile OS Market Share")

plt.show()
# ⭐ Program 8: Multiple Lines on Same Graph
years = [2018, 2019, 2020, 2021, 2022]
sales_A = [50, 60, 65, 70, 80]
sales_B = [40, 55, 60, 68, 75]

plt.plot(years, sales_A, label="Product A")
plt.plot(years, sales_B, label="Product B")

plt.title("Sales Comparison")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.legend()

plt.show()
# ⭐ Program 9: Adding Grid Lines
x = [1, 2, 3, 4]
y = [2, 5, 8, 10]

plt.plot(x, y)
plt.grid(True)
plt.title("Graph with Grid")

plt.show()
# ⭐ Program 10: Subplots (Multiple Graphs)
x = [1, 2, 3, 4]
y1 = [2, 3, 4, 5]
y2 = [5, 4, 3, 2]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Increasing")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Decreasing")

plt.show()