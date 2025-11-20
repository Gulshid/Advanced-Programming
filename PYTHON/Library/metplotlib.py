# Single Line Plot 
import matplotlib.pyplot as plt
# X - axis values
x = [1,2,3,4,5]
# Y - axis 
y = [2,4,6,8,10]
plt.plot(x,y)

plt.title("SImple Line Plot ")

plt.xlabel("X values ")
plt.ylabel("Y values ")
plt.show()


# Line Plot with Style 
x = [1,2,3,4]
y = [10,20,15,25]
plt.plot(x,y, color = 'green', linestyle ='-', marker = 'o')


plt.title("Style Line Graph ")
plt.show()


