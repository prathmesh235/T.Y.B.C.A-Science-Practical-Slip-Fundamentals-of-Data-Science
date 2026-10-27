import pandas as pd

data = {
    'Name': ['Amit', 'Rahul', 'Priya', 'Sneha', 'Rohan', 'Neha', 'Raj', 'Pooja'],
    'Age': [20, 21, 19, 20, 22, 21, 20, 19],
    'Course': ['BCA', 'BSc', 'BCA', 'BCom', 'BCA', 'BSc', 'BCA', 'BCom'],
    'Marks': [75, 80, 90, 68, 85, 78, 88, 92]
}

df = pd.DataFrame(data)
print(df.head(5))