import pandas as pd

# Create dictionary
data = {
    'Name': ['Amit', 'Rahul', 'Priya', 'Sneha'],
    'Marks': [75, 85, 90, 80],
    'City': ['Pune', 'Mumbai', 'Nashik', 'Nagpur']
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print(df)