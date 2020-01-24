
# Question 1

print(titanic.groupby('sex')['fare'].mean(),'\n')

# Question 2

print(titanic.groupby(['sex','pclass'])['fare'].median(),'\n')

# Question 3

print(pd.crosstab(titanic['survived'],titanic['pclass'], margins=True, normalize = 'columns'))