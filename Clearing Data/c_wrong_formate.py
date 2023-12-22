import pandas as pd

# Data of Wrong Format
"""Cells with data of wrong format can make it difficult, or even impossible, to analyze data.

To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format."""


df = pd.read_csv("./data/csv/data_with_date.csv")


# Convert Into a Correct Format
"""In our Data Frame, we have two cells with the wrong format. Check out row 22 and 26, the 'Date' column should be a string that represents a date:

22        45           NaN    100       119     282.0
23        60  '2020/12/23'    130       101     300.0
24        45  '2020/12/24'    105       132     246.0
25        60  '2020/12/25'    102       126     334.5
26        60      20201226    100       120     250.0
"""

# Let's try to convert all cells in the 'Date' column into dates.
# Pandas has a to_datetime() method for this:
df['Date'] = pd.to_datetime(df['Date'])

# As you can see from the result, the date in row 26 was fixed, but the empty date in row 22 got a NaT (Not a Time) value, in other words an empty value. One way to deal with empty values is simply removing the entire row.
# print(df.loc[[22, 24]])


# Removing Rows
"""The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value, and we can remove the row by using the dropna() method."""
# Remove rows with a NULL value in the "Date" column:
# df.dropna(subset=['Date'], inplace=True)
