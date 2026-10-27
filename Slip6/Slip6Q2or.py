import pandas as pd

# Create dataset
data = {
    'Name': ['Smaran', 'Sachin', 'Samarpan', 'Spandan', 'Shaman'],
    'Address': ['Pune', 'Mumbai', 'Delhi', 'Chennai', 'Madurai'],
    'Age': [20, 23, 19, 21, 22],
    'Class': ['ME', 'MSc (CA)', 'MVoC', 'MCom', 'MSc']
}

# Create DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv('StudentData.csv', index=False)

# Import the dataset
df = pd.read_csv('StudentData.csv')

# a) Display statistical description
print("Statistical Description:")
print(df.describe(include='all'))

# b) Display shape of dataset
print("\nShape of Dataset:")
print(df.shape)

# c) Display first two rows
print("\nFirst Two Rows:")
print(df.head(2))