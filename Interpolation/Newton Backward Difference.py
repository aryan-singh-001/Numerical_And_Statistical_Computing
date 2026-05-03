def newton_backward(x, y, target):
    n = len(x)
    table = np.zeros((n, n))
    table[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            table[i][j] = table[i][j-1] - table[i-1][j-1]
            
    h = x[1] - x[0]
    u = (target - x[-1]) / h
    value = table[n-1, 0]
    u_prod = 1
    
    for i in range(1, n):
        u_prod *= (u + (i - 1))
        value += (u_prod * table[n-1, i]) / math.factorial(i)
    return value