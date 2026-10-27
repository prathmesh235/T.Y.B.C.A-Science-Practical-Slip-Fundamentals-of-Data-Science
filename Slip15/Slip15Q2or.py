import pandas as pd
import matplotlib.pyplot as plt
import os

# Create Data.csv if it does not exist
if not os.path.exists("Data.csv"):
    data = {
        'name': ['Amit', 'Rahul', 'Priya', 'Sneha', 'Rohan'],
        'age': [20, None, 22, 21, None],
        'salary': [25000, 30000, None, 35000, 40000]
    }
    pd.DataFrame(data).to_csv("Data.csv", index=False)

# Read CSV file
df = pd.read_csv("Data1.csv")

print("Original Dataset:")
print(df)

# Replace missing values with column mean
df['salary'] = df['salary'].fillna(df['salary'].mean())
df['age'] = df['age'].fillna(df['age'].mean())

print("\nDataset After Handling Missing Values:")
print(df)

# Line plot: Name vs Salary
plt.plot(df['name'], df['salary'], marker='o')
plt.title("Name vs Salary")
plt.xlabel("Name")
plt.ylabel("Salary")
plt.grid(True)
plt.show()