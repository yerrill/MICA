import matplotlib.pyplot as plt
import numpy as np

# Lake Pollution
def f(x, n):
    if n % 2 == 0:
        return 0.99*x + 10
    else:
        return 0.99*x

x_cache = {}
def x(n):
    # Check/Return Cached items
    if n in x_cache:
        return x_cache[n]

    if n == 0:
        result = 0  # Initial Condition
    elif n > 0:
        result = f(x(n-1), n)

    # Cache and return result
    x_cache[n] = result
    return result

upper_limit = 1_000
n_values = [n for n in range(0, upper_limit)]
x_values = [x(n) for n in n_values]
#print(n_values)
#print(x_values)

# Plot scatter for X_n
plt.scatter(n_values, x_values, s=1)
plt.xlabel("n values")
plt.ylabel("x values")

# Plot line for fish tolerance
plt.plot(n_values, [100_000*0.005 for n in range(0, upper_limit)],
        label="Fish Line", color="Red")
plt.show()
