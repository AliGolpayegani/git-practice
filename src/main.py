import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 4, 6, 8, 10, 12, 14])
y = np.sqrt(x)

print(y)
plt.plot(x, y)

from add import add_func
print(add_func(45,41))

print('Hello World')

print('bye bye!')

a = np.linspace(1, 100, 150)

b = 25
c = ['ali']
d = [i for i in range(100)]

print('finish the merging')

def arbitraryfunc(x):
    x = x ** 2
    x = np.sin(x)
    h = x + np.tan(x)
    return x

a = arbitraryfunc(153)
print(a)