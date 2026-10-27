import pandas as pd

# Create DataFrame
data = {'Price': [100, 200, 300, 400, 500, 600, 700, 800, 900]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Perform equal-width binning
bins = 3
labels = ['Low', 'Medium', 'High']

df['Category'] = pd.cut(df['Price'], bins=bins, labels=labels)

print("\nBinned DataFrame:")
print(df)