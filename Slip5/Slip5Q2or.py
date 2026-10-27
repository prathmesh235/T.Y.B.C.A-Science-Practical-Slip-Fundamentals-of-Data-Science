import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [20, 25, 30, 28, 35, 40, 38, 45, 50, 42, 48, 55]
}

df = pd.DataFrame(data)
print(df)

s = df['Sales']
print("Range:", s.max() - s.min())
print("Variance:", s.var())
print("Standard Deviation:", s.std())