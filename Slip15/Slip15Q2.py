import pandas as pd
import os

# Create data.csv if it does not exist
if not os.path.exists("data.csv"):
    data = {
        'Name': ['Amit', 'Rahul', 'Priya', 'Sneha', 'Rohan'],
        'Marks': [75, 85, 90, 80, 70],
        'Age': [20, 21, 19, 22, 20]
    }
    pd.DataFrame(data).to_csv("data.csv", index=False)

# Read CSV file
df = pd.read_csv("data.csv")

print("DataFrame:")
print(df)

print("\nDescribe:")
print(df.describe())

print("\nHead:")
print(df.head())

print("\nTail:")
print(df.tail())

print("\nMaximum Values:")
print(df.max(numeric_only=True))

print("\nMinimum Values:")
print(df.min(numeric_only=True))