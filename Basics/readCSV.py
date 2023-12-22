import pandas as pd
"""
A simple way to store big data sets is to use CSV files (comma separated files).

CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

In our examples we will be using a CSV file called 'data.csv'.

If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:
if you don't use to_string method"""

df = pd.read_csv('./data/csv/data_168.csv')

# print(df.to_string())  # use to_string() to print the entire DataFrame.

# max_rows
"""The number of rows returned is defined in Pandas option settings.
You can check your system's maximum rows with the pd.options.display.max_rows statement.

In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows."""
# print(pd.options.display.max_rows)

# You can change it as you wish
pd.options.display.max_rows = 100
# print(df)
