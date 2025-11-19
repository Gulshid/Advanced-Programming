import numpy as np
print(" --- Numpy Basics  Tutorial ---")

# # Program 1: NumPy Basics and Array Operations
# # Creating Array 
# list_data = [1,2,3,4,5,6]
# arr1 = np.array(list_data)

# print(f"From list : {arr1}")

# # 2D Array 
# arr2D = np.array([[1,2,3], [4,5,6]])
# print(f"2D Array :\n {arr2D}")

# # Zero Array
# zero_array = np.zeros((3,3))
# print(f"Zero Array : \n {zero_array}")

# # One Array 
# one_array = np.ones((2,5)) # 2 is row and 5 is column
# print(f"One Array : \n {one_array}")


# # Range Array 
# range_array= np.arange(0,10, 2) # start , stop , step 
# print(f"Range Array : \n {range_array}")

# # Random Array 
# random_array = np.random.random((2,3))
# print(f"Ranodm Array : \n {random_array}")

# # ARRAY PROPERTIES
# print("---- Array Properties ---")
# print("Shape  of Array 2D :", arr2D.shape)
# print("Dimension of Array 2D : ", arr2D.ndim)
# print(f"Datatype of Array 2D : { arr2D.dtype}")
# print(f"SIze of Array 2D : {arr2D.size}")
# print(f" Total Byte in Array 2D : {arr2D.nbytes}")


# # Array Operations
# a = np.array([1,2,3,4,5])
# b = np.array([7,8,9,10,11])

# print(f"Displaying a : {a}")
# print(f"Displaying b : {b}")

# print(f" a + b  : {a + b }")
# print(f" a - b  : {a - b }")
# print(f" a * b  : {a * b }")
# print(f" a ** b  : {a ** 2 }") # Square root every element 

# print(f"SIn : {np.sin(a)}")

# # Indexing and Slicing 
# matrix = np.array([[1,2,3,4],
#                     [5,6,7,8],
#                     [1,2,4,5],
#                     [4,5,2,1]
#                 ])
# print("Original Matrix : \n",matrix )
# print("Element at (1,2)", matrix[1,2])
# print("First Row : ", matrix[0 ,:])
# print("Second Column :", matrix[:, 1])
# print("SUb matrix ( first 2 row and last 2 col :) : \n ",matrix[:2,-2:])

# # Array ReShaping 
# flat_arr = np.arange(12)
# reshape = flat_arr.reshape(3,4)
# flattened = reshape.flatten()

# print("Original 1D :",flat_arr )
# print("Reshape to 3 X 4 :", reshape)
# print("Flattend : ",flattened )


# Program 2: Advanced NumPy Operations
# Mathematical Operations

data = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]   
    ])
# 1. Mathematical Operations
print("Data :\n", data)
print("sum of all Element :", np.sum(data))
print("Sum Along column :", np.sum(data, axis = 0))
print("sum Along Row :", np.sum(data, axis = 1))
print("Mean :", np.mean(data))
print("standard Deviation :", np.std(data))
print("Minimium :", np.min(data))
print("maximium :", np.max(data))

# 2. Boolean Indexing
number = np.array([1,2,3,4,5,6,7,8,9,10])
print("Numbers :", number)

greater_than_5 = number[number > 5]
print("Number is greater than 5 :", greater_than_5)

even_number = number[number % 2 == 0]
print("Number in Even Number :", even_number)


# 3. Linear Algebra Operations
A = np.array([
    [1,2], [3,4]
    ])
B = np.array([
    [2,3], [5,4]
    ])

print("Matrix of A : \n", A)
print("Matrix of B : \n", B)

matrix_product = np.dot(A, B)
print("Dot Product :", matrix_product)


det_A = np.linalg.det(A)
det_B = np.linalg.det(B)
inv_A = np.linalg.inv(A)
inv_B = np.linalg.inv(B)
print(f"Det of A : { det_A:.2f}")
print(f"Det of B :{ det_B:.2f}")

print(f"Inverse of A : { inv_A}")
print(f"Inverse of B :{ inv_B}")

# 4. Statistical Operations

scores = np.array([85, 92, 78, 90, 88, 76, 95, 89, 84, 91])
print(f"test Score : {scores}")
print(f"Averge  Score : {np.mean(scores):.2f}")
print(f"Median  Score : {np.median(scores):.2f}")
print(f"Range Score : {np.ptp(scores)}")
print(f"variance  Score : {np.var(scores)}")
print(f"25 Percentile  Score : {np.percentile(scores, 25)}")
print(f"75Percentile  Score : {np.percentile(scores, 75)}")

# 5. Working with NaN values
data_with_nan = np.array([1, 2, np.nan, 4, 5, np.nan, 7])
print("Data with NaN :", data_with_nan)

clean_data = data_with_nan[~np.isnan(data_with_nan)]
print("Removed   NaN :", clean_data)

mean_val = np.nanmean(data_with_nan)
filled_data = np.where(np.isnan(data_with_nan), mean_val, data_with_nan)
print(f" Data with NaN filled : {filled_data}")

# 6. Broadcasting
matrix = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])

vector = np.array([10,20,30])

result = matrix + vector
print(f" Matrix : {matrix}")
print(f" vector : {vector}")
print(f" Original Array  : {result}")


# 7. File I/O with NumPy
sample_data = np.random.randint(0, 100, (5, 5))
print(f" Sample data to save : {sample_data}")

np.savetxt('sample_data.csv : ', sample_data,delimiter=',', fmt = '%d')
print(f"Data Saved to 'sample_data.csv'")

loaded_data = np.loadtxt('sample_data.csv', delimiter =',')
print(f"Loaded data : {loaded_data}")
