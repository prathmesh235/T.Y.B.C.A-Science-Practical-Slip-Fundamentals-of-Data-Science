import numpy as np
import matplotlib.pyplot as plt

# Generate 50 random integers
data = np.random.randint(10, 100, 50)

# Line Chart
plt.figure()
plt.plot(data, marker='o')
plt.title("Line Chart")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)
plt.show()

# Scatter Plot
plt.figure()
plt.scatter(range(50), data)
plt.title("Scatter Plot")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()

# Histogram
plt.figure()
plt.hist(data, bins=10, edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Box Plot
plt.figure()
plt.boxplot(data)
plt.title("Box Plot Before Adding Outliers")
plt.ylabel("Value")
plt.show()

# Add two outliers
updated_data = np.append(data, [200, 250])

# Updated Box Plot
plt.figure()
plt.boxplot(updated_data)
plt.title("Box Plot After Adding Outliers")
plt.ylabel("Value")
plt.show()