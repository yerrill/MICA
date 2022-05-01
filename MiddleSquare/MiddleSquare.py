import matplotlib.pyplot as plt
import numpy as np
import random

def middleValue(val):
    s = str(val)
    l = len(s)
    lower = int(l/2 - 2)
    upper = int(l/2 + 2)

    nVal = s[lower:upper]

    return int(nVal)


def generate_values(val, upperlimit=100):
    x_values = [n for n in range(0, upperlimit)]
    y_values = []

    value = val

    for n in x_values:
        square_value = value**2
        next_value = middleValue(square_value)
        y_values.append(value)
        value = next_value

    return x_values, y_values

# ------------------------------------------------------------------------------

for n in range(0, 5):
    num = random.randint(1000, 9999)
    print(num)
    x, y = generate_values(num, 150)
    plt.scatter(x, y, label=str(num))



#x_vals, y_vals = generate_values(3791)
#print(y_vals)

# Matplotlib
#plt.scatter(x_vals, y_vals)
plt.legend()
plt.show()
