import pandas as pd

# Read the Iris dataset CSV file
df = pd.read_csv(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",
    header=None
)

# Assign column names
df.columns = [
    'SepalLength', 'SepalWidth',
    'PetalLength', 'PetalWidth', 'Species'
]

print("Dataset:")
print(df.head())

print("\nDataset Description:")
print(df.describe())

print("\nMean of Numeric Attributes:")
print(df.mean(numeric_only=True))

print("\nMissing Values:")
print(df.isnull().sum())

print("\nAny Missing Values:", df.isnull().values.any())

############################