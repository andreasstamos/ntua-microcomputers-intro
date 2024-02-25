import numpy as np
from matplotlib import pyplot as plt

ns = np.arange(5000)
y1 = 10 + 10 + 20000 / ns
y2 = 30 + 10 + 10000 / ns
y3 = 2 + 2 + 100000 / ns
y4 = 1 + 1 + 200000 / ns


plt.figure()
plt.plot(ns, y1, label="Discrete Components")
plt.plot(ns, y2, label="FPGA")
plt.plot(ns, y3, label="SoC-1")
plt.plot(ns, y4, label="SoC-2")
plt.legend()
plt.xlabel("Quantity")
plt.ylabel("Cost per item [euros]")
plt.show()
