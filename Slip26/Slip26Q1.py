import numpy as np
from sklearn import preprocessing

# Create NumPy array
data = np.array([10, 20, 30, 40, 50])

print("Original Data:")
print(data)

# Standardize the data
standardized_data = preprocessing.scale(data)

print("\nStandardized Data:")
print(standardized_data)