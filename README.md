# Numerical Methods Implementation in Python

This repository contains a comprehensive collection of numerical methods used in computational mathematics. These tools are designed to solve engineering and scientific problems involving root-finding, linear systems, and data interpolation.

---

## 📂 Project Structure

The codebase is organized into functional modules based on the mathematical objective of each method:
```text
numerical_methods_project/
├── root_finding/             # Solvers for f(x) = 0
│   ├── bisection.py          # Halving interval method
│   ├── regula_falsi.py       # False position method
│   └── newton_raphson.py     # Gradient-based solver
├── linear_systems/           # Solvers for Ax = B
│   ├── gauss_elimination.py  # Direct row-reduction
│   ├── jacobi_iterative.py   # Basic iterative solver
│   └── gauss_seidel.py       # Improved iterative solver
└── interpolation/            # Data estimation
    ├── newton_forward.py     # Forward difference
    └── newton_backward.py    # Backward difference
