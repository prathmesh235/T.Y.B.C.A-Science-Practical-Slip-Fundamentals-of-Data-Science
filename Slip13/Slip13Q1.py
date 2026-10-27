import pandas as pd

# Create a sample dataset
data = {
    'Name': ['Amit', 'Rahul', 'Priya', 'Sneha', 'Rohan'],
    'Age': [20, 21, 19, None, 22],
    'Marks': [75, 80, 85, 70, None]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nShape:", df.shape)
print("Size:", df.size)

print("\nData Types:")
print(df.dtypes)

print("\nStatistical Details:")
print(df.describe())

print("\nNumber of Observations:", len(df))

print("\nMissing Values:")
print(df.isnull().sum())