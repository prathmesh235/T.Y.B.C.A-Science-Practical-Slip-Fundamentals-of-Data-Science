import numpy as np

# Ages of 10 employees
ages = np.array([25, 30, 28, 35, 40, 26, 32, 29, 45, 31])

# Calculate statistics
print("Employee Ages:", ages)
print("Minimum Age:", np.min(ages))
print("Maximum Age:", np.max(ages))
print("Average Age:", np.mean(ages))