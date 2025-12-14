import pandas as pd

data = {
    "Name": ["ALice", "Bob", "Charlie", "Diana"],
    "Age": [25,39,23,49],
    "City": ["New york", "london", "Tokyo", "paris"],
    "Salary": [50000, 60000, 70000, 80000]
}

df = pd.DataFrame(data)
print(df)

print("Shape:", df.shape)
print("col", df.columns.tolist())
print("Data type :", df.dtypes)
print("First two row :", df.head(2))
print("display Name col :", df["Name"])
print("row at index 1 :", df.iloc[1])
print("Statistics :", df.describe())