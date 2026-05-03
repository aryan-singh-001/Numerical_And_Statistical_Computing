def f(x):
    # Example: x^3 - x - 2
    return x**3 - x - 2

def regula_falsi(a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Regula Falsi fails: f(a) and f(b) must have opposite signs.")
        return None
    
    for i in range(max_iter):
        # Calculate the point using the False Position formula
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        
        # Check if the result is within tolerance
        if abs(f(c)) < tol:
            return c
        
        # Decide the side to repeat the steps
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

# Example Usage:
root = regula_falsi(1, 2)
print(f"Regula Falsi Root: {root}")