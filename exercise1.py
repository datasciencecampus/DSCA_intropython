# Question 1

# The number of rows and columns
n_rows, n_cols = titanic.shape
print(f"There are {n_rows} rows and {n_cols} columns in the data\n")

# The data types of the columns
print(titanic.dtypes, '\n')

# Get a list of column names
colnames = list(titanic.columns)
print(colnames,"\n")

# Question 2
fares = titanic['fare']
print(fares.tail(),"\n")

# Question 3
print(titanic[colnames[-1]].head(),'\n')

# Question 4
print(titanic[titanic.columns[1:4]].head())
