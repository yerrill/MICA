import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

r_val = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]  # Rank, x
n_val = [96499, 26057, 10501, 4183, 2861, 913, 509, 298, 158, 85, 31, 19, 8, 3]  # Occurances, y

log_r_val = [np.log(r) for r in r_val]  # Log values, x
log_n_val = [np.log(n) for n in n_val]  # Log values, y

#print(len(r_val), len(n_val), len(log_r_val), len(log_n_val))  # Debugging information
#print(r_val, "\n", n_val, "\n", log_r_val, "\n", log_n_val)


def z(r, A, z):  # Zipf's Law
	return A*(r**z)

def f(x, m, b):  # Linear Equation
	return m*x + b

plt.scatter(r_val, n_val, label="(1a) Linear-Linear Scatter Plot")  # 1a
plt.xlabel("r")
plt.ylabel("n")

#plt.scatter(log_r_val, n_val, label="(1b) Log-Linear Scatter Plot")  # 1b
#plt.xlabel("log r")
#plt.ylabel("n")

#plt.scatter(r_val, log_n_val, label="(1c) Linear-Log Scatter Plot")  # 1c
#plt.xlabel("r")
#plt.ylabel("log n")

#plt.scatter(log_r_val, log_n_val, label="(1d) Log-Log Scatter Plot")  # 1d / 2a
#plt.xlabel("log r")
#plt.ylabel("log n")

#param, cov = curve_fit(f, log_r_val, log_n_val)  # 2b, Line of best Fit
#print(*param)  # -1.073121586396731 12.394727328954843
#domain = np.arange(log_r_val[0], log_r_val[-1], 0.1)
#plt.plot(domain, f(domain, *param), label="Line of Best Fit", color="red")

param, cov = curve_fit(z, r_val, n_val)  # 3, Curve of best fit
print(*param)  # 1126022.8400433052 -1.7748319987527623
domain = np.arange(r_val[0], r_val[-1], 0.1)
plt.plot(domain, z(domain, *param), label="Curve of Best Fit", color="red")

plt.show()