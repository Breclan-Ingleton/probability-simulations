import numpy as np
import matplotlib.pyplot as plt

num_samples = 10000
sample_size = 30

samples = np.random.randint(1, 7, size=(num_samples, sample_size))
sample_means = samples.mean(axis=1)

plt.hist(sample_means, bins=40)

plt.title("Central Limit Theorem: Dice Roll Sample Means")
plt.xlabel("Sample mean")
plt.ylabel("Frequency")

plt.savefig("central_limit_theorem.png", dpi=300, bbox_inches="tight")
plt.show()
