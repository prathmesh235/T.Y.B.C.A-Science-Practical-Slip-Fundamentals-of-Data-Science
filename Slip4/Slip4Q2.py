import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Salary': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 200]
})

s = df['Salary']

print("Q1, Q2, Q3:\n", s.quantile([0.25, 0.50, 0.75]))
print("\nPercentiles:\n", s.quantile([0.25, 0.50, 0.75, 0.90]))

# IQR Method
Q1, Q3 = s.quantile(0.25), s.quantile(0.75)
IQR = Q3 - Q1
outliers_iqr = s[(s < Q1 - 1.5 * IQR) | (s > Q3 + 1.5 * IQR)]

# Z-score Method
z = (s - s.mean()) / s.std()
outliers_z = s[abs(z) > 3]

print("\nIQR Outliers:", outliers_iqr.tolist())
print("Z-score Outliers:", outliers_z.tolist())