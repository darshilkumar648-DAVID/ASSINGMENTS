import numpy as np

# NO. 1 #
identity_matrix = np.eye(3, dtype=float)
print(identity_matrix)

# NO. 2 #
random_array = np.random.rand(10)
print(random_array)

# NO. 3 #
random_int_2d = np.random.randint(0, 100, size=(3, 4))
print(random_int_2d)

# NO. 4 #
custom_array = np.fromfunction(lambda i: i**2, (10,), dtype=int)
print(custom_array)

# NO. 5 #
arr_1d = np.arange(12)
arr_2d = arr_1d.reshape(3, 4)
print(arr_2d)

# NO. 6 #
ones_array = np.ones((3, 3))
print(ones_array)

# NO. 7 #
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
common = np.intersect1d(a, b)
print(common)

# NO. 8 #
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
result = np.setdiff1d(a, b)
print(result)

# NO. 9 #
a = np.arange(15)
np.set_printoptions(threshold=6)
print(a)

# NO. 10 #
arr = np.array([1,2,3,np.nan,5,6,7,np.nan])
result = arr[~np.isnan(arr)]
print(result)

# NO. 11 #

    # 1D array
arr1 = np.arange(1, 21)
print(arr1)
    # 2D array
arr2 = np.arange(1, 21).reshape(4, 5)
print(arr2)

# NO. 12 #
arr = np.arange(24).reshape(2, 3, 4)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Dimensions:", arr.ndim)
print("Data Type:", arr.dtype)

    # Change data type
arr_float = arr.astype(np.float64)
print("New Data Type:", arr_float.dtype)

# NO. 13 #
arr = np.arange(12)
reshaped = arr.reshape(3, 4)
flattened = reshaped.ravel()
print("Original:", arr)
print("Flattened:", flattened)
print("Same array?", np.array_equal(arr, flattened))

# NO. 14 #
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# NO. 15 #
a = np.array([[1],
              [2],
              [3]])   # Shape (3,1)
b = np.array([10, 20, 30])  # Shape (3,)
result = a + b
print(result)

# NO. 16 #
arr = np.random.randint(0, 11, size=(4, 5))
print("Original Array:\n", arr)
mask = arr > 5
print("Boolean Mask:\n", mask)
arr[arr > 5] = 5
print("Modified Array:\n", arr)

# NO. 17 #
arr = np.random.randint(1, 50, size=(4, 4))
print("Array:\n", arr)
# Entire second row
second_row = arr[1, :]
# Last column
last_column = arr[:, -1]
# First two rows and first two columns
subarray = arr[:2, :2]
print("Second Row:", second_row)
print("Last Column:", last_column)
print("Subarray:\n", subarray)

# NO. 18 #
data = np.array([10, 20, 30, 40, 50])
mean = np.mean(data)
std = np.std(data)
print("Mean:", mean)
print("Standard Deviation:", std)
    #🔹 AI 
inputs = np.array([1, 0, 1])
weights = np.array([0.5, 0.2, 0.8])
output = np.sum(inputs * weights)
print("AI Output:", output)
    #🔹 ML
X = np.array([1, 2, 3, 4])
w = 2
b = 1
y = w * X + b
print("Predictions:", y)
    #🔹 DL (Deep Learning)
x = np.array([-2, -1, 0, 1, 2])
relu = np.maximum(0, x)
print("ReLU Output:", relu)

# NO. 19 #
A = np.random.randint(1, 10, size=(4, 4))
print("Matrix A:\n", A)
eigenvalues, eigenvectors = np.linalg.eig(A)
# Reconstruct matrix
A_reconstructed = eigenvectors @ np.diag(eigenvalues) @ np.linalg.inv(eigenvectors)
print("Eigenvalues:\n", eigenvalues)
print("Reconstructed Matrix:\n", A_reconstructed)

# NO. 20 #
arr = np.arange(27)
arr_3d = arr.reshape(3, 3, 3)
flattened = arr_3d.flatten()
print("Original:", arr)
print("Flattened:", flattened)
print("Same?", np.array_equal(arr, flattened))

# NO. 21 #
A = np.random.randint(1, 10, (2, 3))
B = np.random.randint(1, 10, (3, 2))
result_dot = np.dot(A, B)
result_at = A @ B
print("np.dot result:\n", result_dot)
print("@ result:\n", result_at)
    # Performance Comparison (Large Data)
import time
A = np.random.rand(1000, 1000)
B = np.random.rand(1000, 1000)
start = time.time()
np.dot(A, B)
print("np.dot time:", time.time() - start)
start = time.time()
A @ B
print("@ time:", time.time() - start)

# NO. 22 #
A = np.random.randint(1, 10, (2, 1, 4))
B = np.random.randint(1, 10, (4, 1))
    # Broadcasting
result = A + B.T
print("Broadcast Result:\n", result)
result2 = A + B.T[np.newaxis, :, :]
print("Using newaxis:\n", result2)

# NO. 23 #
arr23 = np.random.rand(4, 5)
print("Original Array:\n", arr23)
mask = arr23 < 0.5
arr23[mask] = arr23[mask] ** 2
print("Modified Array:\n", arr23)

# NO. 24 #
arr24 = np.arange(1, 26).reshape(5, 5)
print("Original Array:\n", arr24)
    # Diagonal elements
diagonal = np.diag(arr24)
print("Diagonal Elements:", diagonal)
    # Replace middle row with zeros
arr24[2, :] = 0
print("After replacing middle row:\n", arr24)
    # Flip vertically
flip_vertical = np.flipud(arr24)

    # Flip horizontally
flip_horizontal = np.fliplr(arr24)
print("Flip Vertical:\n", flip_vertical)
print("Flip Horizontal:\n", flip_horizontal)

# NO. 25 #
arr25 = np.random.randint(0, 10, size=(2, 3, 4, 5))
print("Shape:", arr25.shape)
    # Extract subarray
subarray = arr25[0, :, :, :]
print("Subarray Shape:", subarray.shape)
    # Mean along axis
mean_axis = np.mean(arr25, axis=2)
print("Mean along axis=2:\n", mean_axis)

# NO. 26 #
arr26 = np.random.randint(1, 100, size=(10, 20))
print("Original Shape:", arr26.shape)

reshape1 = arr26.reshape(20, 10)
reshape2 = arr26.reshape(5, 40)

print("Reshape (20,10):", reshape1.shape)
print("Reshape (5,40):", reshape2.shape)

print("Size:", arr26.size)
print("Dimensions:", arr26.ndim)

# NO. 27 #
large_arr = np.arange(100).reshape(10, 10)
print("Original Shape:", large_arr.shape)
reshaped = large_arr.reshape(20, 5)
print("Reshaped (20,5):", reshaped.shape)
    # Unravel index example
index = np.unravel_index(55, large_arr.shape)
print("Unravel index of 55:", index)

# NO. 28 #
matrix = np.random.randint(1, 20, size=(6, 6))
print("Original Matrix:\n", matrix)
    # Upper triangular
upper = np.triu(matrix)
    # Set lower triangular to zero
matrix[np.tril_indices(6, -1)] = 0
print("Upper Triangular Matrix:\n", upper)
print("Matrix after setting lower part to zero:\n", matrix)