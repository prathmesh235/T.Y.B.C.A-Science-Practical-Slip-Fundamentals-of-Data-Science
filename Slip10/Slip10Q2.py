import pandas as pd
import numpy as np

data = {
    'emp_name': ['Amit', 'Rahul', 'Priya'],
    'age': [25, 28, 24],
    'salary': [25000, 30000, 28000]
}

df = pd.DataFrame(data)

new_rows = pd.DataFrame({
    'emp_name': ['Amit', 'Rahul', None],
    'age': [25, None, 35],
    'salary': [25000, 30000, None]
})

df = pd.concat([df, new_rows], ignore_index=True)
df['Department'] = np.nan

print("Shape:", df.shape)
print(df)