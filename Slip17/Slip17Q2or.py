import pandas as pd

# Create Employee DataFrame
data = {
    'Employee_ID': range(1, 16),
    'Department': ['IT', 'HR', 'Sales', 'IT', 'HR',
                   'Sales', 'IT', 'HR', 'Sales', 'IT',
                   'HR', 'Sales', 'IT', 'HR', 'Sales'],
    'Age': [25, 30, 28, 32, 27, 35, 29, 26, 31, 33, 24, 36, 28, 34, 30],
    'Salary': [30000, 35000, 28000, 40000, 32000,
               38000, 42000, 31000, 36000, 45000,
               29000, 41000, 39000, 34000, 37000]
}

df = pd.DataFrame(data)

print("Employee DataFrame:")
print(df)

# 1. Simple Random Sampling: Select 5 employees
print("\nSimple Random Sampling:")
print(df.sample(n=5, random_state=1))

# 2. Systematic Sampling: Select every 3rd employee
print("\nSystematic Sampling:")
print(df.iloc[::3])

# 3. Stratified Sampling: Select one employee from each department
print("\nStratified Sampling:")
print(df.groupby('Department', group_keys=False).sample(
    n=1, random_state=1
))