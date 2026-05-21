# Probability Simulations in Python

This project uses Python simulations to build intuition for key probability results.

## Law of Large Numbers

The file `law_of_large_numbers.py` simulates 10,000 dice rolls and plots the running average.

The expected value of one fair die roll is 3.5. As the number of rolls increases, the running average gets closer to 3.5.

This demonstrates the Law of Large Numbers.

## Central Limit Theorem

The file `central_limit_theorem.py` simulates 10,000 samples of 30 dice rolls.

It calculates the mean of each sample and plots the distribution of these sample means.

The histogram becomes roughly bell-shaped, showing the Central Limit Theorem.

## Monte Carlo Probability

The file `monte_carlo_probability.py` estimates the probability that the sum of two fair dice is at least 10.

It does this by simulating 100,000 pairs of dice rolls and calculating the proportion where the total is 10, 11, or 12.

This demonstrates how Monte Carlo simulation can estimate probabilities using repeated random trials.

## Distribution Simulations

## Files

- `law_of_large_numbers.py` — simulates dice rolls and shows the running average approaching the expected value.
- `central_limit_theorem.py` — simulates sample means and shows the Central Limit Theorem.
- `monte_carlo_probability.py` — estimates a probability using repeated random trials.
- `distributions.py` — compares simulated and theoretical means/variances for common distributions.
The file `distributions.py` simulates Binomial, Poisson, and Geometric random variables.

It compares the simulated mean and variance with the theoretical mean and variance for each distribution.

This shows how repeated simulation can confirm theoretical probability results.
