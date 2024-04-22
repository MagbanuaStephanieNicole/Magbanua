import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 10)

y1 = x**2 - 10
y2 = x**3 + x - 100
y3 = x**10 - x**8 + x**2 - 8
y4 = x**4 + x**3 + x**2 + 1
y5 = x**2 + x + 10 / 2*x

plt.figure(figsize=(5, 5))

plt.plot(x, y1, label=r"$a(x) = x^4 + 8$", color='r', linestyle='--')
plt.plot(x, y2, label=r"$b(x) = x^3 + x - 100$", color='b', linestyle=':')
plt.plot(x, y3, label=r"$c(x) = x^(10) - x^8 + x^2 - 8$", color='k', linestyle='-.')
plt.plot(x, y4, label=r"$d(x) = x^4 + x^3 + x^2 + 1$", color='g', linestyle='--')
plt.plot(x, y5, label=r"$e(x) = x^2 + x + 10 / 2x$", color='m', linestyle=':')


plt.axhline(y=0, color='k', linestyle='-', linewidth=2)
plt.axvline(x=0, color='k', linestyle='-', linewidth=2)

plt.title("Graphs")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.legend()

plt.show()