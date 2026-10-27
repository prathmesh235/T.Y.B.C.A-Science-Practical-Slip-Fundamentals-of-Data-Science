import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Create dataset
data = {
    'Country': ['India', 'USA', 'France', 'India', 'USA'],
    'Purchased': ['Yes', 'No', 'Yes', 'No', 'Yes']
}

df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)

print("Original Dataset:")
print(df)

# a. One-Hot Encoding on Country column
df = pd.get_dummies(df, columns=['Country'], dtype=int)

print("\nAfter One-Hot Encoding:")
print(df)

# b. Label Encoding on Purchased column
le = LabelEncoder()
df['Purchased'] = le.fit_transform(df['Purchased'])

print("\nAfter Label Encoding:")
print(df)