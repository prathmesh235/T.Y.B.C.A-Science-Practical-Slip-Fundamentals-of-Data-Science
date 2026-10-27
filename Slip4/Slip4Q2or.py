import pandas as pd

data = {
    'Name': ['Shrikrishna', 'Shridhar', 'Mohan', 'Govind', 'Vasudev'],
    'Address': ['Trivendram', 'Madurai', 'Suchindram', 'Rameswaram', 'Kanyakumari'],
    'Age': [20, None, 19, 21, 22],
    'Class': ['BE', 'BSc(CA)', 'BVoC', 'BCom', 'BSc']
}

# Create and save CSV file
df = pd.DataFrame(data)
df.to_csv('StudentData.csv', index=False)

# Import dataset
df = pd.read_csv('StudentData.csv')

# Replace missing Age with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

print(df)