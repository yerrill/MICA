import numpy as np
import random
import matplotlib.pyplot as plt

N = 10_000
A = 1
X = 100
bin_indices = np.arange(1, X, 1) - 0.5

#numbers = range(1, 100)
#counts = random.choices(numbers, k=N)
#plt.hist(counts, bins=bin_indices)
#plt.xlabel("Bins")
#plt.ylabel("Frequencies")
#plt.title("Random Numbers")

def f(x):
    return 4*x*(1 - x)

def g(x):
    return A / np.sqrt(x*(1 - x))  # Domain (0, 1)

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

counts = [int(100*x(n)) for n in range(1, N)]

approx_x = [n for n in range(2, X)]
approx_y = [g(n) for n in range(2, X)]

#plt.hist(counts, bins=bin_indices)

#plt.xlabel("Bins")
#plt.ylabel("Frequencies")
#plt.title("Logistic Map Orbit")


plt.scatter([n for n in range(1, N)], counts, s=1.0)
plt.show()