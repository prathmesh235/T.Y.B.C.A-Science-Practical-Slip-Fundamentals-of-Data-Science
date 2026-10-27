import matplotlib.pyplot as plt

# Numerical dataset
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

# Create Figure and Axes objects
fig, ax = plt.subplots(figsize=(8, 5))

# Plot the dataset
ax.plot(x, y, color='blue', linewidth=2.5,
        marker='o', markersize=7, linestyle='-')

# Customize the graph
ax.set_title("Numerical Dataset", fontsize=16)
ax.set_xlabel("X Values", fontsize=12)
ax.set_ylabel("Y Values", fontsize=12)
ax.grid(True, linestyle='--', alpha=0.6)

# Display the graph
plt.tight_layout()
plt.show()