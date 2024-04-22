import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 10)

y6 = np.sin(x) / 3*x
y7 = x**3 + 2*x**2 - 10*x + 3
y8 = np.cos(x) / 5*x
y9 = x**3 / 2*x - 10*x
y10 = x+2 * x+3 * x-4

plt.figure(figsize=(5, 5))

plt.plot(x, y6, label=r"$f(x) = np.sin(x) / 3x$", color='r', linestyle='--')
plt.plot(x, y7, label=r"$g(x) = x^3 + 2x^2 - 10x + 3$", color='b', linestyle=':')
plt.plot(x, y8, label=r"$h(x) = np.cos(x) / 5x$", color='k', linestyle='-.')
plt.plot(x, y9, label=r"$i(x) = x^3 / 2*x - 10*x$", color='g', linestyle='--')
plt.plot(x, y10, label=r"$j(x) = (x+2)(x+3)(x-4)$", color='m', linestyle=':')


plt.axhline(y=0, color='k', linestyle='-', linewidth=2)
plt.axvline(x=0, color='k', linestyle='-', linewidth=2)

plt.title("Graphs")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.legend()

plt.show()