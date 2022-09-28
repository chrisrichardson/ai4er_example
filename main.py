
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,4*np.pi,100)
y = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y)
plt.plot(x, y2)
plt.show()
