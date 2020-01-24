
# read in titanic-revised dataset
titanic_revised = pd.read_excel('../Data/titanic_revised.xlsx')

# Create unique id field
titanic_revised['name_age_id'] = titanic_revised['name'] + " " + titanic_revised['age'].astype(str)

# Merge the titanic datasets

#Question 1

# left is the obvious choice for this join
titanic_merge2 = titanic.merge(titanic_revised[['name_age_id','boat','body','home.dest']], how = 'left', on = 'name_age_id')

# outer join works too
#titanic_merge2 = titanic.merge(titanic_revised[['name_age_id','boat','body','home.dest']], how = 'outer', on = 'name_age_id')
print('Left and Outer joins work for merging these datasets.\n')

# Question 2
print("counts of observations in 'boat', 'body', and 'home.dest'")
print(titanic_merge2[['boat','body','home.dest']].count(),'\n')

# Question 3

print("{} passengers used lifeboat 3.".format(len(titanic_merge2[titanic_merge2['boat'] == '3'])))
print("The proportion of female passengers in lifeboat 3 was {}.\n".format(titanic_merge2[titanic_merge2['boat'] == '3']['sex'].value_counts(normalize=True)['female']))

# Question 4
NY_count = (titanic_merge2['home.dest'].str.contains('NY') | titanic_merge2['home.dest'].str.contains('New York')).sum()
print("{} passengers are listed as having either home or destination as 'New York' or 'NY' in the data".format(NY_count))
