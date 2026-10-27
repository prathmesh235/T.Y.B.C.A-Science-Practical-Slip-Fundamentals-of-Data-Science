import pandas as pd
import numpy as np

# 1. Create DataFrame with 10 rows
df = pd.DataFrame({
    'emp_name': ['Amit', 'Rahul', 'Priya', 'Sneha', 'Rohan',
                 'Neha', 'Raj', 'Pooja', 'Kiran', 'Anil'],
    'age': [25, 28, 24, 30, 27, 26, 29, 23, 31, 28],
    'salary': [25000, 30000, 28000, 35000, 32000,
               27000, 40000, 26000, 45000, 30000]
})

# 2. Apply shape() and describe()
print("Shape:", df.shape)
print("\nDescription:\n", df.describe())

# 3. Add 5 rows with duplicates and missing values
new_rows = pd.DataFrame({
    'emp_name': ['Amit', 'Rahul', 'Meena', None, 'Kiran'],
    'age': [25, None, 22, 35, 31],
    'salary': [25000, 30000, None, 38000, 45000]
})

df = pd.concat([df, new_rows], ignore_index=True)

# Add Department column with empty values
df['Department'] = np.nan

print("\nFinal DataFrame:\n", df)