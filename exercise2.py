# Question 1

print(titanic[titanic['name'] == 'Birkeland, Mr. Hans Martin Monsen'],"\n")

# Question 2

print(f"{len(titanic[titanic['sex'] == 'male'])} passengers are male.\n")

# Question 3

print(f"{len(titanic[titanic['age'] < 18])} passengers are children.\n")

# Question 4
total_rows = len(titanic)
survive_rows = len(titanic[titanic['survived'] == 1])
print("The proportion of survivors is {:.2f}".format(survive_rows/total_rows))