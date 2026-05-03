import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    matrix = np.hstack([A, b.reshape(-1, 1)]).astype(float)

    for i in range(n):
        for j in range(i + 1, n):
            ratio = matrix[j, i] / matrix[i, i]
            matrix[j, i:] -= ratio * matrix[i, i:]

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (matrix[i, n] - np.dot(matrix[i, i+1:n], x[i+1:n])) / matrix[i, i]
    return x