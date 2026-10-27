import pandas as pd

# Create student DataFrame
data = {
    'Roll No': [1, 2, 3, 4, 5],
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Rohan'],
    'Percentage': [75, 80, 85, 80, 90]
}

df = pd.DataFrame(data)

print("Student DataFrame:")
print(df)

# Calculate mean, median and mode
print("\nMean:", df['Percentage'].mean())
print("Median:", df['Percentage'].median())
print("Mode:", df['Percentage'].mode().tolist())