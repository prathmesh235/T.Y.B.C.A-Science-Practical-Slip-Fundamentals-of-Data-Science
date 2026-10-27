import pandas as pd
import numpy as np

# Create dataset
data = {
    'Name': ['Shyama', 'Shreeji', 'Ramya', 'Radha', 'Satya'],
    'Address': ['Pune', 'Mumbai', 'Delhi', 'Mumbai', 'Pune'],
    'Age': [20, 19, np.nan, 21, 22],
    'Class': [
        'BSc (Chemistry)', 'BSc (Physics)', 'BSc (Biology)',
        'BSc (Zoology)', 'BSc (CS)'
    ]
}

# Create DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv('StudentData.csv', index=False)

# Import dataset
df = pd.read_csv('StudentData.csv')

print("Original Dataset:")
print(df)

# Replace missing Age with mean age
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Apply one-hot encoding to Address
df = pd.get_dummies(df, columns=['Address'], dtype=int)

print("\nDataset After Preprocessing:")
print(df)