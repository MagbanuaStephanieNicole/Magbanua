import numpy as np

import numpy as np

def matrix_multiplication():
    print("Matrix multiplication:")
    A = np.array([[10, 25], [25, 98]])
    B = np.array([[76, 33], [26, 77]])
    result = np.dot(A, B)
    print(result)

def vector_dot_product():
    print("Vector dot product:")
    A = np.array([57, 6, 25])
    B = np.array([17, 5, 24])
    result = np.dot(A, B)
    print(result)

def matrix_vector_multiplication():
    print("Matrix-vector multiplication:")
    A = np.array([[98, 76], [34, 23]])
    x = np.array([76, 64])
    result = np.dot(A, x)
    print(result)

def transpose_matrix():
    print("Transpose of a matrix:")
    A = np.array([[5, 7], [6, 8], [2, 0]])
    result = np.transpose(A)
    print(result)

def transpose_vector():
    print("Transpose of a vector:")
    v = np.array([6, 2, 1])
    result = np.transpose(v)
    print(result)

def transpose_3d_array():
    print("Transpose of a 3D array:")
    A = np.arange(24).reshape(2, 3, 4)
    result = np.transpose(A, (1, 0, 2))
    print(result)

def inverse_matrix():
    print("Inverse of a square matrix:")
    A = np.array([[5, 6], [2, 7]])
    result = np.linalg.inv(A)
    print(result)

def inverse_singular_matrix():
    print("Inverse of a singular matrix:")
    A = np.array([[5, 6], [2, 7]])
    try:
        result = np.linalg.inv(A)
        print(result)
    except np.linalg.LinAlgError as e:
        print(e)

def inverse_3x3_matrix():
    print("Inverse of a 3x3 matrix:")
    A = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
    result = np.linalg.inv(A)
    print(result)


def determinant_matrix():
    print("Determinant of a square matrix:")
    A = np.array([[5, 6], [2, 7]])
    result = np.linalg.det(A)
    print(result)

def determinant_singular_matrix():
    print("Determinant of a singular matrix:")
    A = np.array([[5, 6], [2, 7]])
    result = np.linalg.det(A)
    print(result)

def determinant_3x3_matrix():
    print("Determinant of a 3x3 matrix:")
    A = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
    result = np.linalg.det(A)
    print(result)

def flatten_2d_array():
    print("Flatten a 2D array:")
    A = np.array([[0, 1, 4], [5, 6, 0]])
    result = A.flatten()
    print(result)

def flatten_3d_array():
    print("Flatten a 3D array:")
    A = np.arange(60).reshape(3, 4, 5)
    result = A.flatten()
    print(result)

def flatten_order_F():
    print("Flatten a 2D array and order in 'F' style:")
    A = np.array([[1, 2, 3], [0, 1, 4]])
    result = A.flatten(order='F')
    print(result)



# dot method
print("DOT METHOD EXAMPLES -----------------------------------------------------------")
print()
matrix_multiplication()
print()
vector_dot_product()
print()
matrix_vector_multiplication()

print()
print()
print()

# transpose method
print("\nTRANSPOSE METHOD EXAMPLES -----------------------------------------------------------")
print()
transpose_matrix()
print()
transpose_vector()
print()
transpose_3d_array()

print()
print()
print()

# linalg.inv method
print("\nlinalg.inv METHOD EXAMPLES -----------------------------------------------------------")
print()
inverse_matrix()
print()
inverse_singular_matrix()
print()
inverse_3x3_matrix()

print()
print()
print()

# linalg.det method
print("\nlinalg.det METHOD EXAMPLES -----------------------------------------------------------")
print()
determinant_matrix()
print()
determinant_singular_matrix()
print()
determinant_3x3_matrix()
print()

print()
print()
print()

# flatten method
print("\nFLATTEN METHOD EXAMPLES ----------------------------------------------------------- ")
print()
flatten_2d_array()
print()
flatten_3d_array()
print()
flatten_order_F()

print()
print()
print()
