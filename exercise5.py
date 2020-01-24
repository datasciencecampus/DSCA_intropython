
# Question 1

print("The oldest passenger is {} years old.\n".format(titanic['age'].max()))

# Question 2

print(titanic['sex'].value_counts(),'\n')

# Question 2b

print(titanic['sex'].value_counts(normalize = True),'\n')

# Question 3

titanic['std_fare'] = (titanic['fare'] - titanic['fare'].mean())/titanic['fare'].std()
print(titanic['std_fare'].head(),'\n')

# Question 4

print("There are {} children in second class".format(titanic[titanic['pclass'] == 2]['child'].sum()))