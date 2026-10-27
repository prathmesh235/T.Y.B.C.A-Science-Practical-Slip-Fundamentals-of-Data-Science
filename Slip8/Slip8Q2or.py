import pandas as pd
import numpy as np

# Create DataFrame of salaries (in thousands)
data = {
    'Salary': [25, 30, 35, 40, 45, 50, 55, 60,
               65, 70, 75, 80, 85, 90, 200]
}

df = pd.DataFrame(data)

print("Employee Salaries (in thousands):")
print(df)

# Calculate quartiles
Q1 = df['Salary'].quantile(0.25)
Q2 = df['Salary'].quantile(0.50)
Q3 = df['Salary'].quantile(0.75)

print("\nQuartiles:")
print("Q1:", Q1)
print("Q2:", Q2)
print("Q3:", Q3)

# Calculate selected percentiles
print("\nPercentiles:")
for p in [25, 50, 75, 90]:
    print(f"{p}th percentile:", df['Salary'].quantile(p / 100))

# Detect outliers using IQR method
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

iqr_outliers = df[
    (df['Salary'] < lower) | (df['Salary'] > upper)
]

print("\nOutliers using IQR method:")
print(iqr_outliers)

# Detect outliers using Z-score method
mean = df['Salary'].mean()
std = df['Salary'].std(ddof=0)

df['Z-score'] = (df['Salary'] - mean) / std

z_outliers = df[abs(df['Z-score']) > 3]

print("\nOutliers using Z-score method (|Z| > 3):")
print(z_outliers)