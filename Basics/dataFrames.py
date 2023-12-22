import pandas as pd

# What is a DataFrame?
"""A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns."""

data = {
    "calaroies": [320, 480, 670],
    "duration": [40, 50, 80]
}

table = pd.DataFrame(data)
# print(table)

# Locate Row
""""Pandas use the loc attribute to return one or more specified row(s)"""
# print(table.loc[0])

"""
This example returns a Pandas Series.
To see many rows at once
"""
# print(table.loc[[0, 1]])  # use a list of indexes:


# It uses the Index to name the row
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
# print(df)

# refer to the named index:
# print(df.loc["day2"])

# Load Files Into a DataFrame
"""
If your data sets are stored in a file, Pandas can load them into a DataFrame.
Load a comma separated file (CSV file) into a DataFrame:
"""
df_csv = pd.read_csv("./data/csv/data_168.csv")
# print(df_csv)
