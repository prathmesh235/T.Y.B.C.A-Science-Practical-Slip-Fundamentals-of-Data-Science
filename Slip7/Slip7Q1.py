import pandas as pd

# Create staff dataset
data = {
    'staff_id': [101, 102, 103, 104, 105],
    'employee_name': ['Amit', 'Rahul', 'Priya', 'Sneha', 'Rohan'],
    'department': ['IT', 'HR', 'Finance', 'IT', 'Sales'],
    'monthly_salary': [30000, 25000, 35000, 32000, 28000]
}

# Create DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv('staff.csv', index=False)

# Read CSV file using Pandas
df = pd.read_csv('staff.csv')

# Display DataFrame
print(df)