import numpy as np

num_simulations = 100000

# Binomial: number of successes in 10 trials, success probability 0.5
binomial_samples = np.random.binomial(n=10, p=0.5, size=num_simulations)

print("Binomial(10, 0.5)")
print("Simulated mean:", np.mean(binomial_samples))
print("Theoretical mean:", 10 * 0.5)
print("Simulated variance:", np.var(binomial_samples))
print("Theoretical variance:", 10 * 0.5 * 0.5)
print()

# Poisson: average rate 3
poisson_samples = np.random.poisson(lam=3, size=num_simulations)

print("Poisson(3)")
print("Simulated mean:", np.mean(poisson_samples))
print("Theoretical mean:", 3)
print("Simulated variance:", np.var(poisson_samples))
print("Theoretical variance:", 3)
print()

# Geometric: number of trials until first success, success probability 0.25
geometric_samples = np.random.geometric(p=0.25, size=num_simulations)

print("Geometric(0.25)")
print("Simulated mean:", np.mean(geometric_samples))
print("Theoretical mean:", 1 / 0.25)
print("Simulated variance:", np.var(geometric_samples))
print("Theoretical variance:", (1 - 0.25) / (0.25 ** 2))
