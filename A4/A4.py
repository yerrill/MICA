import numpy as np
import random
import matplotlib.pyplot as plt

hours = np.arange(0, 100) + 1

def r_exp(n):
    return 100 * (((1 + 0.01) * 0.9) + ((1 + 0.06) * 0.1)) ** n

def r(x):
    if random.random() < 0.9:
        return 0.01
    else:
        return 0.06

def f(x):
    return (1 + r(x))*x

x_cache = {}
def x(n):
    if n in x_cache:
        return x_cache[n]

    if n == 0:
        result = 100
    elif n > 0:
        result = f(x(n-1))

    x_cache[n] = result
    return result


#def dev()


iterations = 20

population = []
sums_pop = [0 for n in hours]
running_dev_sum = [0 for n in hours]

dangerous_level = 0

for n in range(0, iterations):
    x_cache = {}
    population = [x(i) for i in hours]
    running_dev_sum = list(map(lambda x, y, z: x + (y - r_exp(z)) ** 2, running_dev_sum, population, hours))
    plt.scatter(hours, population, s=1.0)
    sums_pop = list(map(lambda x, y: x + y, sums_pop, population))
    if population[-1] > 500:
        dangerous_level += 1


# X bar
sample_mean_pop = [(i/iterations) for i in sums_pop]
plt.scatter(hours, sample_mean_pop, c='Orange', s=10.0, alpha=0.5)

# E(x)
expected = [r_exp(n) for n in hours]
plt.scatter(hours, expected, c='Blue', s=10.0, alpha=0.5)

# Standard Deviation
deviation = [round(np.sqrt(i/iterations), 3) for i in running_dev_sum]
print(deviation)

# Dangerous Level Probability
dangerous_prob = dangerous_level / iterations
print(dangerous_prob)


plt.xlabel("Hours")
plt.ylabel("Population")
plt.title(f"{iterations} Iterations w Sample Mean Population (Orange) & Expected (Blue)")
plt.show()