import numpy as np
import matplotlib.pyplot as plt

# Create NumPy array of ages of 15 employees
ages = np.array([22, 25, 28, 30, 35, 40, 25, 28, 32, 35,
                 45, 50, 30, 38, 42])

# Define custom bins
bins = [20, 30, 40, 50, 60]

# Compute frequency of ages in each bin
frequency, bin_edges = np.histogram(ages, bins=bins)

# Display frequency
print("Age Groups and Frequencies:")
for i in range(len(frequency)):
    print(f"{bin_edges[i]}-{bin_edges[i+1]}: {frequency[i]}")

# Plot histogram
plt.hist(ages, bins=bins, edgecolor='black')
plt.xlabel("Employee Ages")
plt.ylabel("Frequency")
plt.title("Histogram of Employee Ages")
plt.xticks(bins)
plt.show()