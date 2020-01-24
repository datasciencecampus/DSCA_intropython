# Question 1

n_c2_3 = len(titanic[titanic['pclass'].isin([2,3])])
print("{:.1f}% of passengers were in 2nd and 3rd class.\n".format(n_c2_3/len(titanic)*100))

# Question 2

num_solo = len(titanic[(titanic['sibsp'] == 0)&(titanic['parch'] == 0)])
print(f"There are {num_solo} solo travelers in the dataset.\n")

# Question 3

total_em = len(titanic[titanic['embarked'].isin(['C','Q'])])
survive_em = len(titanic[titanic['embarked'].isin(['C','Q']) & (titanic['survived'] == 1)])
print("The proportion of Cherbourg and Queenstown passengers who survived was: {survive_em/total_em:.2f}")