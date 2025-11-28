import pandas as pd
# Program 1: Creating and Exploring DataFrames
print("=== 1 Creating and Exploring dataframe ===")
data = {
    'Name' : ['Alice ', 'bob', 'charlie', 'diana'],
    'Age' : [25, 30, 35, 28],
    'City' : ['New York', 'London', 'Tokyo', 'Paris'],
    'Salary ': [50000, 60000, 70000, 55000]   
}

# create dataframe 
df = pd.DataFrame(data)
print(df)

print()

print("====== 2.Data Frame Information ====")
print(f"Shape : {df.shape}")
print(f"Column : {df.columns.tolist()}")
print(f"Datatype : \n {df.dtypes}")
print()


# Accessing Data
print("====== 3.Accessing Data =======")
print(f"First 2 Row : {df.head(2)}")
print(f"Name and Column : {df['Name']}")
print("Row at index 1 : ", df.iloc[1])
print()


print("===== 4.basic Statistics ====")
print(df.describe())
# Program 2: Data Selection and Filtering

