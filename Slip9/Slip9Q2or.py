import pandas as pd
from pathlib import Path

# Get the folder of this Python file
file_path = Path(__file__).parent / "employee.csv"

# Create employee.csv if it does not exist
if not file_path.exists():
    data = {
        'Employee': ['Amit', 'Rahul', 'Priya', 'Sneha', 'Rohan',
                     'Neha', 'Raj', 'Pooja', 'Kiran', 'Anil'],
        'Salary': [25000, 30000, 28000, 35000, 32000,
                   27000, 40000, 26000, 45000, 50000]
    }
    pd.DataFrame(data).to_csv(file_path, index=False)

# Read CSV file
df = pd.read_csv(file_path)

print("Employee Dataset:")
print(df)

# Calculate descriptive statistics
salary = df['Salary']

print("\nDescriptive Statistics of Salary")
print("Count:", salary.count())
print("Mean:", salary.mean())
print("Median:", salary.median())
print("Variance:", salary.var())
print("Standard Deviation:", salary.std())
print("Minimum:", salary.min())
print("Maximum:", salary.max())
print("Q1 (25%):", salary.quantile(0.25))
print("Q2 (50%):", salary.quantile(0.50))
print("Q3 (75%):", salary.quantile(0.75))