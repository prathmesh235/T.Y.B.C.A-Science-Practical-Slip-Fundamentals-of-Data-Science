import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Create dataset
data = {
    'Name': ['Smaran', 'Sachin', 'Samarpan', 'Spandan', 'Shravan'],
    'Address': ['Pune', 'Mumbai', 'Delhi', 'Chennai', 'Madurai'],
    'Age': [20, 23, 19, 21, 22],
    'Class': ['BE', 'BSc(CS)', 'BVoC', 'BCom', 'BSc']
}

df = pd.DataFrame(data)
df.to_csv('StudentData.csv', index=False)

# Import dataset
df = pd.read_csv('StudentData.csv')
print("Original Dataset:\n", df)

# One-Hot Encoding on Name
df = pd.get_dummies(df, columns=['Name'], dtype=int)

# Label Encoding on Class
le = LabelEncoder()
df['Class'] = le.fit_transform(df['Class'])

print("\nEncoded Dataset:\n", df)