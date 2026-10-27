import pandas as pd
import os

# Create sample CSV file if it does not exist
if not os.path.exists("employee.csv"):
    data = {
        'Employee': ['Amit', 'Rahul', 'Priya', 'Sneha', 'Rohan'],
        'Salary': [25000, 30000, 35000, 40000, 45000]
    }
    pd.DataFrame(data).to_csv("employee.csv", index=False)

# Read CSV file
df = pd.read_csv("employee.csv")

print("DataFrame:")
print(df)

print("\nDescribe:")
print(df.describe())

print("\nFirst 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nMaximum Values:")
print(df.max(numeric_only=True))

print("\nMinimum Values:")
print(df.min(numeric_only=True))