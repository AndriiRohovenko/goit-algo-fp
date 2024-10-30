import random
import matplotlib.pyplot as plt

def roll_dice():
    """Simulate rolling two dice and return their sum."""
    return random.randint(1, 6) + random.randint(1, 6)

def monte_carlo_simulation(num_rolls):
    """Simulate dice rolls using the Monte Carlo method."""
    sums_count = {i: 0 for i in range(2, 13)}  # Initialize count for each possible sum (2-12)

    # Simulate dice rolls
    for _ in range(num_rolls):
        dice_sum = roll_dice()
        sums_count[dice_sum] += 1

    # Calculate probabilities for each sum
    probabilities = {dice_sum: count / num_rolls for dice_sum, count in sums_count.items()}
    return probabilities

def plot_probabilities(probabilities):
    """Plot Monte Carlo."""
    sums = list(probabilities.keys())
    monte_carlo_probs = list(probabilities.values())
    plt.figure(figsize=(10, 6))
    plt.bar(sums, monte_carlo_probs, color='skyblue', label='Monte Carlo')
    plt.xlabel("Sum of Two Dice")
    plt.ylabel("Probability")
    plt.title("Monte Carlo Simulation")
    plt.legend()
    plt.show()



# Run simulation
num_rolls = 100000  # Large number for better approximation
monte_carlo_probs = monte_carlo_simulation(num_rolls)
print(monte_carlo_probs)

# Plot results
plot_probabilities(monte_carlo_probs)

print("Sum | Monte Carlo Probability | Analytical Probability")
for dice_sum in sorted(monte_carlo_probs.keys()):
    print(f"{dice_sum:>3} | {monte_carlo_probs[dice_sum]:>20.4f}")
