import numpy as np
from sklearn.preprocessing import normalize

# Create numerical dataset
data = np.array([[3, 4], [6, 8], [5, 12]])

print("Original Data:")
print(data)

# Perform unit-length normalization
normalized_data = normalize(data, norm='l2')

print("\nNormalized Data:")
print(normalized_data)