import pandas as pd

# Empty Cells
# Empty cells can potentially give you a wrong result when you analyze data.


# Remove Rows
"""One way to deal with empty cells is to remove rows that contain empty cells.

This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result."""

df = pd.read_csv("./data/csv/data_168.csv")

# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
new_df = df.dropna()

# print(new_df.to_string())

# If you want to change the original DataFrame, use the inplace = True argument:
"""df.dropna(inplace=True)
print(df.to_string())"""


# Replace Empty Values
"""Another way of dealing with empty cells is to insert a new value instead.

This way you do not have to delete entire rows just because of some empty cells.

The fillna() method allows us to replace empty cells with a value:"""

df.fillna(130, inplace=True)
# print(df.to_string())


# Replace Only For Specified Columns
"""The example above replaces all empty cells in the whole Data Frame.

To only replace empty values for one column, specify the column name for the DataFrame:"""
df['Calories'].fillna(130, inplace=True)


# Replace Using Mean, Median, or Mode
"""A common way to replace empty cells, is to calculate the mean, median or mode value of the column.

Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:"""
# Calculate the MEAN, and replace any empty values with it:
# Mean = the average value (the sum of all values divided by number of values).
x = df['Calories'].mean()
df['Calories'].fillna(x, inplace=True)

# Median = the value in the middle, after you have sorted all values ascending.
x = df['Calories'].median()
df['Calories'].fillna(x, inplace=True)

# Mode = the value that appears most frequently.
x = df['Calories'].mode()[0]  # mode gives two columns thats why we use 0
print(x)
df['Calories'].fillna(x, inplace=True)
# print(df.to_string())
