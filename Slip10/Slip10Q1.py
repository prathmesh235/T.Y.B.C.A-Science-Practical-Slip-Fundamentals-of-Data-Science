import pandas as pd

# Create student DataFrame
data = {
    'student_id': [101, 102, 103, 104, 105],
    'name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Rohan'],
    'marks': [75, 80, 85, 80, 90]
}

df = pd.DataFrame(data)

print("Student DataFrame:")
print(df)

# Calculate mean, median and mode
print("\nMean:", df['marks'].mean())
print("Median:", df['marks'].median())
print("Mode:", df['marks'].mode().tolist())