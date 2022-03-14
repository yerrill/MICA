import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

N = 10_000
X = 100

def f(x):
    return 4*x*(1 - x)

def g(x, A):
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

def z(n, A):
    return g(n/100, A)*100


logistic_bins = np.arange(1, X, 1) - 0.5  # Histogram plotting
orbit = [int(X*x(n)) for n in range(1, N)]  # Formerly counts
unique, counts = np.unique(orbit, return_counts=True)  # Frequency Scatter
unique = np.delete(unique, 0)  # Remove 0 which would cause a domain error
counts = np.delete(counts, 0)

v, _ = curve_fit(z, unique, counts, bounds=(0, np.inf))

func_y = [z(n, v[0]) for n in unique]
#print(func_y)
print(v)

plt.hist(orbit, bins=logistic_bins, rwidth=0.25)
plt.scatter(unique, counts, s=5.0, c="Green")
plt.scatter(unique, func_y, s=5.0, c="Red")


plt.xlabel("Bins")
plt.ylabel("Frequencies")
plt.title("Logistic Map Orbit Frequency vs Curve Fit")

plt.show()
