import numpy as np
# program NO 1
# 1D array
lits_2 = [1,2,3,3]
# method 1
arr_9 = np.array(lits_2)
print("Method 1:\n",arr_9)

# method 2
arr_1d = np.array([1,2,3,4,5])
print("1 D array using numpy :\n", arr_1d)

# method 1
# 2D array
arr_2D = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]])
print("Multiple array using numpy :\nmethod 1: \n",arr_2D)

# method 2
arr_11 = ([1,2,3], [4,5,6])
arr_num = np.array(arr_11)
print("Method 2 :\n",arr_num)


#  Zero_Array
zero_arr = np.zeros((3,5))
print("Zero Array :\n", zero_arr)

# Ones Array 
one_arr = np.ones((2,4))
print("Ones array :\n",one_arr)

# Range array 
range_arr = np.arange(1,11,2)
print("Range array :\n", range_arr)

# Random array 
random_arr = np.random.random((3,4))
print("Random Array :\n", random_arr)


# Array Properties
print("*** Array Properties ***")
print("Shape of 2D Array :\n", arr_num.shape)
print("DImensional of 2D array :", arr_num.ndim)
print("Datatype of 2d array :", arr_num.dtype)
print("Size of 2d array :", arr_num.size)
print("total bytes  of 2d array :", arr_num.nbytes)

print(f"SIn : {np.sin(arr_num)}")


# Indexing and SLicing 
matrix = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])

print("Original Matrix :", matrix)
print("specific index 1,3:", matrix[1,3])
print("First row : \n", matrix[0,:])
print("second row : \n", matrix[1,:])
print("third row : \n", matrix[2,:])
print("Fourth row : \n", matrix[3,:])


print("first col :\n", matrix[:, 0])
print("second col :\n", matrix[:, 1])
print("third col :\n", matrix[:, 2])
print("fourth col :\n", matrix[:, 3])

print("Two row and col :", matrix[:2, 2:])

# Array Reshaping
flat_arr = np.arange(12)
reshape_arr = flat_arr.reshape(3, 4)

flattened = reshape_arr.flatten()

print("flat_arr :", flat_arr)
print("reshape arr :\n", reshape_arr)
print("flattened arr :", flattened)




