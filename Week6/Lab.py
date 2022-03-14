import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.optimize import curve_fit

numbers = random.choices(range(1, 100), k=20_000)
bin_indices = np.arange(1, 100, 1)-0.5

plt.hist(numbers, bins=bin_indices, ec="White")

def f(x):
    return 2*round(np.minimum(x, 1-x), 9)  # Logistic map in A3

x_cache = {}
def x(n):
    if n in x_cache:
        return x_cache[n]

    if n == 0:
        result = 0.123456789
    elif n > 0:
        result = f(x(n-1))

    x_cache[n] = result
    return result

x_values = [int(100*x(n)) for n in range(1, 20_000)]
#print(x_values)
plt.hist(x_values, bins=bin_indices, color="Red")

plt.show()
