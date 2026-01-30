# pandas dataframe with computed column
import pandas as pd

data = {
    "A": [1,2,2,1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

# create a dataFrame from the data in the dictionary
df = pd.DataFrame(data)

# create a new column from the existing columns
df["D"] = df["A"] + df["C"]

# print the new data frame with the new column
print(df)
