import numpy as np
print(" --- Numpy Basics  Tutorial ---")


# Creating Array 
list_data = [1,2,3,4,5,6]
arr1 = np.array(list_data)

print(f"From list : {arr1}")

# 2D Array 
arr2D = np.array([[1,2,3], [4,5,6]])
print(f"2D Array :\n {arr2D}")

# Zero Array
zero_array = np.zeros((3,3))
print(f"Zero Array : \n {zero_array}")

# One Array 
one_array = np.ones((2,5)) # 2 is row and 5 is column
print(f"One Array : \n {one_array}")


# Range Array 
range_array= np.arange(0,10, 2) # start , stop , step 
print(f"Range Array : \n {range_array}")

# Random Array 
random_array = np.random.random((2,3))
print(f"Ranodm Array : \n {random_array}")

# ARRAY PROPERTIES
print("---- Array Properties ---")
print("Shape  of Array 2D :", arr2D.shape)
print("Dimension of Array 2D : ", arr2D.ndim)
print(f"Datatype of Array 2D : { arr2D.dtype}")
print(f"SIze of Array 2D : {arr2D.size}")
print(f" Total Byte in Array 2D : {arr2D.nbytes}")


# Array Operations
a = np.array([1,2,3,4,5])
b = np.array([7,8,9,10,11])

print(f"Displaying a : {a}")
print(f"Displaying b : {b}")

print(f" a + b  : {a + b }")
print(f" a - b  : {a - b }")
print(f" a * b  : {a * b }")
print(f" a ** b  : {a ** 2 }") # Square root every element 

print(f"SIn : {np.sin(a)}")

# Indexing and Slicing 
matrix = np.array([[1,2,3,4],
                    [5,6,7,8],
                    [1,2,4,5],
                    [4,5,2,1]
                ])
print("Original Matrix : \n",matrix )
print("Element at (1,2)", matrix[1,2])
print("First Row : ", matrix[0 ,:])
print("Second Column :", matrix[:, 1])
print("SUb matrix ( first 2 row and last 2 col :) : \n ",matrix[:2,-2:])

# Array ReShaping 
flat_arr = np.arange(12)
reshape = flat_arr.reshape(3,4)
flattened = reshape.flatten()

print("Original 1D :",flat_arr )
print("Reshape to 3 X 4 :", reshape)
print("Flattend : ",flattened )