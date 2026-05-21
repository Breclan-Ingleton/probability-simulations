import numpy as np
import matplotlib.pyplot as plt

n = 10000

rolls = np.random.randint(1, 7, size=n)
running_average = np.cumsum(rolls) / np.arange(1, n + 1)

plt.plot(running_average)
plt.axhline(3.5, linestyle="--")

plt.title("Law of Large Numbers: Dice Rolls")
plt.xlabel("Number of rolls")
plt.ylabel("Running average")

plt.show()
