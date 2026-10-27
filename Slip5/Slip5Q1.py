import pandas as pd

data = {
    'Laptop_Model': ['HP', 'Dell', 'Lenovo', 'Asus', 'Acer'],
    'Cost': [45000, 50000, 40000, 55000, 35000]
}

df = pd.DataFrame(data)
print(df)