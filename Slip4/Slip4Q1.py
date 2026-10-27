import pandas as pd

data = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Mouse', 'Keyboard', 'Monitor', 'Printer', 'Speaker'],
    'Brand': ['HP', 'Samsung', 'Apple', 'Dell', 'Logitech', 'LG', 'Canon', 'Sony'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Accessories', 'Accessories', 'Electronics', 'Electronics', 'Accessories'],
    'Price': [50000, 25000, 40000, 500, 1200, 15000, 8000, 3000]
}

df = pd.DataFrame(data)
print(df.head(5))