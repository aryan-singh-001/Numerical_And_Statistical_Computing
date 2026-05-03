def gauss_seidel(A, b, x0, tol=1e-5, max_iter=100):
    x = x0.copy().astype(float)
    for _ in range(max_iter):
        x_old = x.copy()
        for i in range(len(b)):
            sum_j = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x_old[i+1:])
            x[i] = (b[i] - sum_j) / A[i, i]
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            break
    return x

# For Jacobi, simply use x_old for all terms in the sum instead of the updated x.