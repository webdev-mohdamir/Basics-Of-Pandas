import pandas as pd

# View the data

# The head() method returns the headers and a specified number of rows, starting from the top.
"""Note: if the number of rows is not specified, the head() method will return the top 5 rows."""
df = pd.read_csv('./data/csv/data_168.csv')
# print(df.head(10))  # displays the first 10 rows

# The tail() method returns the headers and a specified number of rows, starting from the bottom.
# print(df.tail())

# Info About the Data
"""The DataFrames object has a method called info(), that gives you more information about the data set."""
print(df.info())  # it will show many things including non-null values
