import numpy as np
import random
import matplotlib.pyplot as plt

# WARNING: May need to resize window to see full plots

# https://en.wikipedia.org/wiki/Lehmer_random_number_generator

N = 100_000  # Range of X

m = 2_147_483_647  # (2**31) - 1, Parameters of RNG
a = 48271

bins = 250  # Number of bins to use


def f(x):
    return (a*x)%m


x_cache = {}
def x(n):
    if n in x_cache:
        return x_cache[n]

    if n == 0:
        result = 2
    elif n > 0:
        result = f(x(n-1))
    
    x_cache[n] = result
    return result


bin_indices = np.arange(0, m, np.ceil(m / bins))  # Create 100 bins in range [0, m]

counts = [x(n) for n in range(1, N)]  # Calculate orbit

fig, axs = plt.subplots(1, 2)  # Create multiplot
fig.suptitle(f"Lehmer's RNG, n = {N}")


# Create Scatter Plot

#plt.scatter([n for n in range(1, N)], counts, s=1.0)
#plt.xlabel("i value")
#plt.ylabel("X_i value")
#plt.title(f"Logistic Map Orbit, n = {N}")
axs[0].scatter([n for n in range(1, N)], counts, s=1.0)
axs[0].set_xlabel("i value")
axs[0].set_ylabel("X_i value")
axs[0].set_title("Logistic Map Orbit")


# Create Histogram

#plt.hist(counts, bins=bin_indices)
#plt.xlabel("Bins")
#plt.ylabel("Frequencies")
#plt.title(f"Frequency of visiting, bin size = {int(np.ceil(m / bins))}")
axs[1].hist(counts, bins=bin_indices)
axs[1].set_xlabel(f"{bins} Bins, size = {int(np.ceil(m / bins))}")
axs[1].set_ylabel("Frequencies")
axs[1].set_title("Frequency of visiting")


plt.show()