
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)
y2 = np.cos(x)
y3 = y/y2

plt.plot(x, y)
plt.plot(x, y2)
plt.plot(x, y3)
plt.ylim((-4, 4))

plt.show()
