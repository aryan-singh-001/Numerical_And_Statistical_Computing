def df(x):
    return 3*x**2 - 1  # Derivative of x^3 - x - 2

def newton_raphson(x0, tol):
    x = x0
    while abs(f(x)) > tol:
        x = x - f(x) / df(x)
    return x

print(f"Newton-Raphson Root: {newton_raphson(1.5, 0.0001)}")