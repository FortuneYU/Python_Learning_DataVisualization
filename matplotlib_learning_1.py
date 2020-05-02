# encoding:utf-8
# learning how to use matplotlib to draw fiigures

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm as cm

# define data

x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)
y1 = np.random.rand(100)

plt.scatter(x, y1, c="r", label="scatter figure")

plt.plot(x, y, ls="--", lw=2, label="plot figure")

plt.legend()

plt.savefig("D:\\PycharmProjects\\\matplotlib_learning\\figure.png")

plt.show()
