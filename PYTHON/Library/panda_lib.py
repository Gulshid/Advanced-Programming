# ======================= PANDAS COMPLETE PRACTICE =======================

import pandas as pd
import numpy as np

# ================= Program 1: Creating & Exploring DataFrame =================
print("\n=== Program 1: Creating and Exploring DataFrames ===\n")

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, 30, 35, 28],
    "City": ["New York", "London", "Tokyo", "Paris"],
    "Salary": [50000, 60000, 70000, 55000]
}
df = pd.DataFrame(data)

print(df)
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Data Types:\n", df.dtypes)
print("\nFirst 2 rows:\n", df.head(2))
print("\nName column:\n", df["Name"])
print("\nRow at index 1:\n", df.iloc[1])
print("\nStatistics:\n", df.describe())

# ================= Program 2: Selection & Filtering =================
print("\n=== Program 2: Data Selection and Filtering ===\n")

data = {
    "Student": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
    "Math": [85, 92, 78, 88, 65, 95],
    "Science": [90, 88, 82, 92, 70, 96],
    "English": [78, 85, 80, 79, 72, 90],
    "Grade": ["B", "A", "C", "B", "D", "A"]
}
df = pd.DataFrame(data)

print(df)
print("\nSelected Columns:\n", df[["Student", "Math"]])
print("\nMath > 85:\n", df[df["Math"] > 85])
print("\nMath > 80 AND Science > 85:\n", df[(df["Math"] > 80) & (df["Science"] > 85)])
print("\nGrade A:\n", df.query("Grade == 'A'"))
print("\nEnglish > 80 (Student & Science):\n",
      df.loc[df["English"] > 80, ["Student", "Science"]])

# ================= Program 3: Adding & Modifying Columns =================
print("\n=== Program 3: Adding and Modifying Columns ===\n")

data = {
    "Employee": ["Alice", "Bob", "Charlie", "Diana"],
    "Department": ["IT", "HR", "IT", "Finance"],
    "Base_Salary": [50000, 45000, 55000, 48000],
    "Years_Experience": [3, 5, 2, 4]
}
df = pd.DataFrame(data)

df["Bonus"] = df["Base_Salary"] * 0.10
df["Total_Salary"] = df["Base_Salary"] + df["Bonus"]
df["Base_Salary"] *= 1.05

def experience_level(y):
    if y >= 5:
        return "Senior"
    elif y >= 3:
        return "Mid-Level"
    return "Junior"

df["Experience_Level"] = df["Years_Experience"].apply(experience_level)
df["High_Earner"] = np.where(df["Total_Salary"] > 50000, "Yes", "No")

print(df)

# ================= Program 4: Handling Missing Data =================
print("\n=== Program 4: Handling Missing Data ===\n")

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": [25, np.nan, 35, 28, np.nan],
    "Salary": [50000, 60000, np.nan, 55000, 48000],
    "Department": ["IT", "HR", "IT", np.nan, "Finance"]
}
df = pd.DataFrame(data)

print(df)
print("\nMissing values count:\n", df.isnull().sum())

df_filled = df.copy()
df_filled["Age"].fillna(df_filled["Age"].mean(), inplace=True)
df_filled["Salary"].fillna(df_filled["Salary"].mean(), inplace=True)
df_filled["Department"].fillna(df_filled["Department"].mode()[0], inplace=True)

print("\nAfter Filling:\n", df_filled)
print("\nAfter Dropping Rows:\n", df.dropna())

# ================= Program 5: GroupBy Analysis =================
print("\n=== Program 5: GroupBy Analysis ===\n")

data = {
    "Salesperson": ["Alice", "Bob", "Charlie", "Alice", "Bob", "Charlie", "Alice"],
    "Region": ["North", "South", "East", "North", "South", "East", "North"],
    "Sales_Amount": [1200, 50, 80, 800, 1100, 45, 75],
    "Month": ["Jan", "Jan", "Jan", "Feb", "Feb", "Feb", "Mar"]
}
df = pd.DataFrame(data)

print("Total Sales:\n", df.groupby("Salesperson")["Sales_Amount"].sum())
print("\nAverage by Region:\n", df.groupby("Region")["Sales_Amount"].mean())
print("\nMultiple Stats:\n",
      df.groupby("Salesperson")["Sales_Amount"].agg(["sum", "mean", "count", "max"]))

# ================= Program 6: Sorting & File Operations =================
print("\n=== Program 6: Sorting and File Operations ===\n")

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": [25, 30, 22, 35, 28],
    "Salary": [50000, 75000, 45000, 80000, 60000],
    "Department": ["IT", "Finance", "IT", "HR", "Finance"]
}
df = pd.DataFrame(data)

print("\nSorted by Age:\n", df.sort_values("Age"))
print("\nSorted by Salary Desc:\n", df.sort_values("Salary", ascending=False))
print("\nSorted Multi:\n", df.sort_values(["Department", "Salary"], ascending=[True, False]))

df.to_csv("employee_data.csv", index=False)
df_csv = pd.read_csv("employee_data.csv")
print("\nRead from CSV:\n", df_csv)
print("\nInfo:")
df_csv.info()
print("\nDescribe:\n", df_csv.describe())

