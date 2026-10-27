import pandas as pd

data = {
    'Name': ['Amit', 'Rahul', 'Priya', 'Sneha', 'Rohan', 'Neha', 'Raj', 'Pooja'],
    'Department': ['IT', 'HR', 'IT', 'Sales', 'HR', 'IT', 'Sales', 'Finance'],
    'Designation': ['Developer', 'Manager', 'Tester', 'Executive', 'Analyst', 'Developer', 'Manager', 'Accountant'],
    'Salary': [30000, 40000, 28000, 25000, 35000, 32000, 45000, 30000]
}

df = pd.DataFrame(data)
print(df.head(5))