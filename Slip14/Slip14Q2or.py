import pandas as pd
import matplotlib.pyplot as plt
import os

# Create sample iris.csv if file does not exist
if not os.path.exists("iris.csv"):
    data = {
        'sepal_length': [5.1, 4.9, 6.3, 5.8, 7.0, 6.5],
        'sepal_width': [3.5, 3.0, 3.3, 2.7, 3.2, 3.0],
        'petal_length': [1.4, 1.4, 6.0, 5.1, 4.7, 5.2],
        'petal_width': [0.2, 0.2, 2.5, 1.9, 1.4, 2.0],
        'species': ['setosa', 'setosa', 'virginica',
                    'virginica', 'versicolor', 'versicolor']
    }
    pd.DataFrame(data).to_csv("iris.csv", index=False)

# Import dataset
df = pd.read_csv("iris.csv")

# Bar plot: Frequency of each species
frequency = df['species'].value_counts()

plt.figure()
frequency.plot(kind='bar', edgecolor='black')
plt.title("Frequency of Iris Species")
plt.xlabel("Species")
plt.ylabel("Frequency")
plt.xticks(rotation=0)
plt.show()

# Histogram: Distribution of petal length for each species
plt.figure()
for species in df['species'].unique():
    plt.hist(df[df['species'] == species]['petal_length'],
             alpha=0.5, label=species)

plt.title("Histogram of Iris Species")
plt.xlabel("Petal Length")
plt.ylabel("Frequency")
plt.legend()
plt.show()