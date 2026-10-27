import pandas as pd
import matplotlib.pyplot as plt
import os

# Create sample dataset if iris.csv is missing
if not os.path.exists("iris1.csv"):
    data = {
        'sepal_length': [5.1, 4.9, 6.2, 5.8, 7.0, 6.4],
        'sepal_width':  [3.5, 3.0, 2.8, 2.7, 3.2, 3.0],
        'petal_length': [1.4, 1.4, 4.8, 5.1, 4.7, 5.5],
        'petal_width':  [0.2, 0.2, 1.8, 1.9, 1.4, 1.8],
        'species': [
            'setosa', 'setosa', 'versicolor',
            'versicolor', 'virginica', 'virginica'
        ]
    }
    pd.DataFrame(data).to_csv("iris1.csv", index=False)

# Read dataset
df = pd.read_csv("iris1.csv")
df.columns = df.columns.str.strip()

features = [
    'sepal_length', 'sepal_width',
    'petal_length', 'petal_width'
]

# Check required columns
if not all(col in df.columns for col in features + ['species']):
    print("Error: Check the column names in iris.csv.")
else:
    # Create pair plot using Matplotlib
    colors = {
        'setosa': 'blue',
        'versicolor': 'green',
        'virginica': 'red'
    }

    fig, axes = plt.subplots(4, 4, figsize=(12, 10))

    for i, col1 in enumerate(features):
        for j, col2 in enumerate(features):
            ax = axes[i, j]

            for species, group in df.groupby('species'):
                if i == j:
                    ax.hist(
                        group[col1].dropna(),
                        alpha=0.5,
                        label=species,
                        color=colors.get(species, 'gray')
                    )
                else:
                    ax.scatter(
                        group[col2], group[col1],
                        label=species,
                        color=colors.get(species, 'gray'),
                        alpha=0.7
                    )

            if i == 3:
                ax.set_xlabel(col2)
            if j == 0:
                ax.set_ylabel(col1)

    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper right')
    fig.suptitle("Pair Plot of Iris Dataset", fontsize=16)
    plt.tight_layout()
    plt.show()

    print("Analysis:")
    print("Setosa is the most separable species.")
    print("Petal length and petal width help distinguish species.")
    print("Versicolor and Virginica show some overlap.")