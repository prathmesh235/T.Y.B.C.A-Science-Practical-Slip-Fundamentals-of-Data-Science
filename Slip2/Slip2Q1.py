import pandas as pd

marks = pd.Series([72, 85, 91, 68, 85, 79, 94])

print("Sum:", marks.sum())
print("Average:", marks.mean())
print("Median:", marks.median())
print("Mode:", marks.mode().tolist())
print("Minimum:", marks.min())
print("Maximum:", marks.max())
print("Standard Deviation:", round(marks.std(), 2))