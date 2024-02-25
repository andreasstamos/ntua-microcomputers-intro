import numpy as np
from matplotlib import pyplot as plt

ns = np.logspace(1, 7, 10000)
y1 = ns * (10 + 10) + 20000
y2 = ns * (30 + 10) + 10000
y3 = ns * (2 + 2) + 100000
y4 = ns * (1 + 1) + 200000
min_cost = np.min([y1, y2, y3, y4], axis=0)

plt.figure()
plt.loglog(ns, y1, label="Discrete Components")
plt.loglog(ns, y2, label="FPGA")
plt.loglog(ns, y3, label="SoC-1")
plt.loglog(ns, y4, label="SoC-2")
plt.loglog(ns, min_cost, label="Minimum Total Cost", linewidth=3, linestyle="-.")
plt.legend()
plt.xlabel("Quantity")
plt.ylabel("Total cost [euros]")
plt.grid()
plt.show()
