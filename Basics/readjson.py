import pandas as pd
"""
Big data sets are often stored, or extracted as JSON.

JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.

In our examples we will be using a JSON file

JSON = Python Dictionary

JSON objects have the same format as Python dictionaries."""

df = pd.read_json('./data/json/small.json')
# print(df)

# Check the readCSV.py for explanation
# print(df.to_string())
# pd.options.display.max_rows = 200
# print(df)
