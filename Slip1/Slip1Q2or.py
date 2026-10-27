import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(1, 100, 25)
x = range(1, 26)

print("Random Array:", data)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(x, data, color='blue', marker='o')
plt.title("Line Chart")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.scatter(x, data, color='red')
plt.title("Scatter Plot")
plt.xlabel("Index")
plt.ylabel("Value")

plt.subplot(2, 2, 3)
plt.hist(data, color='green', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.subplot(2, 2, 4)
plt.boxplot(data, patch_artist=True,
            boxprops=dict(facecolor='orange'))
plt.title("Box Plot")
plt.ylabel("Value")

plt.tight_layout()
plt.show()