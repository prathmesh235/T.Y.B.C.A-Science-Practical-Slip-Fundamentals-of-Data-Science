import pandas as pd

# Create two lists
subjects = ['Java', 'Python', 'DBMS', 'FDS', 'CN']
marks = [85, 90, 75, 80, 70]

# Convert lists into DataFrame
df = pd.DataFrame({
    'Subject': subjects,
    'Marks': marks
})

# Display DataFrame
print(df)