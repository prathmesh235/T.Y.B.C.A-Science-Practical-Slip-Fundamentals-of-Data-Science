import pandas as pd

# Create DataFrame
data = {
    'Product': ['Laptop', 'Mobile', 'Keyboard', 'Mouse'],
    'Quantity': [5, 10, 15, 20],
    'Price': [50000, 20000, 1500, 800]
}

df = pd.DataFrame(data)

# Display DataFrame
print("Product DataFrame:")
print(df)

# Calculate total quantity
print("\nTotal Quantity:", df['Quantity'].sum())

# Calculate average price
print("Average Price:", df['Price'].mean())