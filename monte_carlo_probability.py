import numpy as np

num_simulations = 100000

die_1 = np.random.randint(1, 7, size=num_simulations)
die_2 = np.random.randint(1, 7, size=num_simulations)

total = die_1 + die_2

probability_sum_at_least_10 = np.mean(total >= 10)

print("Estimated probability that the sum is at least 10:")
print(probability_sum_at_least_10)
