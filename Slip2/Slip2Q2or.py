import pandas as pd
import numpy as np

data = {'X': [1, 2, 4, 5], 'Y': [3, 4, 6, 8]}
df = pd.DataFrame(data)

print("DataFrame:\n", df)

p1 = df.iloc[0].values
p2 = df.iloc[1].values

diff = p1 - p2
distance = np.linalg.norm(diff)

print("Difference Vector:", diff)
print("Euclidean Distance:", distance)