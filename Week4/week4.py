import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 0.99*x + 5

x_cache = {}
def x(n):
    # Check/Return Cached items
    if n in x_cache:
        return x_cache[n]

    if n == 0:
        result = 456  # Initial Condition
    elif n > 0:
        result = f(x(n-1))

    # Cache and return result
    x_cache[n] = result
    return result

n_values = range(0, 1000)
x_values = [x(n) for n in n_values]
plt.scatter(n_values, x_values, s=1)
plt.show()
