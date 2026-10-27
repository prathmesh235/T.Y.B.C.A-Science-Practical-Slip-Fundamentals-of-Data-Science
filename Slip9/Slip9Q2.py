import numpy as np
import matplotlib.pyplot as plt

# Generate a random array of 50 integers
data = np.random.randint(1, 101, 50)

print("Random Array:")
print(data)

# Create four plots
plt.figure(figsize=(12, 8))

# 1. Line Chart
plt.subplot(2, 2, 1)
plt.plot(data, color='blue', marker='o', linestyle='-')
plt.title("Line Chart")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)

# 2. Scatter Plot
plt.subplot(2, 2, 2)
plt.scatter(range(50), data, color='green', marker='o')
plt.title("Scatter Plot")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)

# 3. Histogram
plt.subplot(2, 2, 3)
plt.hist(data, bins=10, color='orange', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(axis='y')

# 4. Box Plot
plt.subplot(2, 2, 4)
plt.boxplot(data, patch_artist=True)
plt.title("Box Plot")
plt.ylabel("Value")
plt.grid(True)

plt.tight_layout()
plt.show()