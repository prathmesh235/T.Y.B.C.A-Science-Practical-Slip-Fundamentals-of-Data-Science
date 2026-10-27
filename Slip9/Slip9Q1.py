import pandas as pd
from pathlib import Path

# Get the folder containing this Python file
folder = Path(__file__).parent
file_path = folder / "iris.csv"

# Create iris.csv if it does not exist
if not file_path.exists():
    df = pd.DataFrame({
        "Species": (
            ["setosa"] * 50 +
            ["versicolor"] * 50 +
            ["virginica"] * 50
        )
    })
    df.to_csv(file_path, index=False)

# Read CSV file
df = pd.read_csv(file_path)

# Display species frequency
print("Frequency of Iris Species:")
print(df["Species"].value_counts())