import pandas as pd

# What is a Series?
""""
A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.
"""

a = [1, 5, 67, 8]

my_var = pd.Series(a)
# print(my_var)

# Labels
"""
If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

This label can be used to access a specified value.
"""
# print(my_var[0])


# Create Labels
"""With the index argument, you can name your own labels."""

data_with_lables = pd.Series(a, index=["x", "y", "z", "a"])
# print(data_with_lables)
# print(data_with_lables["y"])  # data with the lable of y

# Key/Value Objects as Series
"""You can also use a key/value object, like a dictionary, when creating a Series.
    Note the key will be the lables
"""

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

# print(myvar)

"""To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series."""

my_var = pd.Series(calories, ['day1', 'day2'])
# print(myvar)
