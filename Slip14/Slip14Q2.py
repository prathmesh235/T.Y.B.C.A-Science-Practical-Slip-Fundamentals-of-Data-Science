import pandas as pd
import os

# Create employee.csv if it does not exist
if not os.path.exists("employee.csv"):
    data = {
        'Employee': ['Amit', 'Rahul', 'Priya', 'Sneha', 'Rohan'],
        'Salary': [25000, 30000, 35000, 40000, 45000]
    }
    pd.DataFrame(data).to_csv("employee.csv", index=False)

# Read CSV file
df = pd.read_csv("employee.csv")

print("Employee Dataset:")
print(df)

# Calculate descriptive statistics
salary = df['Salary']

print("\nSalary Descriptive Statistics:")
print("Count:", salary.count())
print("Mean:", salary.mean())
print("Median:", salary.median())
print("Variance:", salary.var())
print("Standard Deviation:", salary.std())
print("Minimum:", salary.min())
print("Maximum:", salary.max())

print("\nQuartiles:")
print(salary.quantile([0.25, 0.50, 0.75]))

print("\nComplete Statistics:")
print(salary.describe())