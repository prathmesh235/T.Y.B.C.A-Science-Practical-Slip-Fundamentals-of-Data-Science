import pandas as pd
import os

# Create CSV if it does not exist
if not os.path.exists("Student_Marks.csv"):
    data = {
        'Student': ['Amit', 'Rahul', 'Priya', 'Sneha', 'Rohan'],
        'Marks': [35, 55, 70, 85, 95]
    }
    pd.DataFrame(data).to_csv("Student_Marks.csv", index=False)

# Read CSV file
df = pd.read_csv("Student_Marks.csv")

print("Dataset Before Discretization:")
print(df)

# Discretize marks
bins = [0, 40, 60, 80, 100]
labels = ['Poor', 'Average', 'Good', 'Excellent']

df['Performance'] = pd.cut(
    df['Marks'],
    bins=bins,
    labels=labels,
    include_lowest=True
)

print("\nDataset After Discretization:")
print(df)