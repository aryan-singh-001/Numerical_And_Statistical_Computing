import numpy as np

def gauss_seidel(A, b, x0=None, tol=1e-5, max_iter=100):
    n = len(b)
    if x0 is None:
        x = np.zeros(n)
    else:
        x = x0.astype(float)
        
    for k in range(max_iter):
        x_old = x.copy()
        
        for i in range(n):
            # Sum of A[i][j] * x[j] for all j != i
            # Uses the most recently updated values of x
            sum_j = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x_old[i+1:])
            x[i] = (b[i] - sum_j) / A[i, i]
            
        # Convergence check (Infinity Norm)
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            print(f"Converged in {k+1} iterations.")
            return x
            
    print("Reached maximum iterations without full convergence.")
    return x

# Example Usage:
# 4x + y + z = 2
# x + 5y + 2z = -6
# x + 2y + 3z = -4
A = np.array([[4, 1, 1], [1, 5, 2], [1, 2, 3]])
b = np.array([2, -6, -4])

solution = gauss_seidel(A, b)
print(f"Gauss-Seidel Solution: {solution}")