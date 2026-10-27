import pandas as pd
import matplotlib.pyplot as plt
import os

# Check if iris.csv exists; otherwise create sample data
if not os.path.exists("iris.csv"):
    data = {
        'sepal_length': [5.1, 4.9, 6.2, 5.8, 7.0, 6.4,
                         5.5, 6.0, 6.7],
        'sepal_width': [3.5, 3.0, 2.8, 2.7, 3.2, 3.0,
                        2.4, 2.9, 3.1],
        'petal_length': [1.4, 1.4, 4.8, 5.1, 4.7, 5.5,
                         3.8, 4.5, 5.6],
        'petal_width': [0.2, 0.2, 1.8, 1.9, 1.4, 1.8,
                        1.1, 1.5, 2.1],
        'species': ['setosa', 'setosa', 'versicolor',
                    'versicolor', 'versicolor', 'virginica',
                    'versicolor', 'virginica', 'virginica']
    }

    pd.DataFrame(data).to_csv("iris.csv", index=False)
    print("Sample iris.csv created successfully.")

# Read CSV file
df = pd.read_csv("iris.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Create box plots
features = [
    'sepal_length',
    'sepal_width',
    'petal_length',
    'petal_width'
]

df.boxplot(column=features, by='species', figsize=(12, 8))

plt.suptitle("Iris Measurements Across Three Species")
plt.title("")
plt.xlabel("Species")
plt.ylabel("Measurement (cm)")
plt.tight_layout()
plt.show()