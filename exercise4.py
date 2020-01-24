# Question 1

titanic['child'] = (titanic['age'] < 18).astype(int)
print(titanic['child'].head(),'\n')

# Question 2

titanic['embarked_city'] = titanic['embarked'].map({'S':'Southampton','C':'Cherbourg','Q':'Queenstown'})
print(titanic['embarked_city'].sample(5),'\n')

# Question 3

titanic['surname'] = titanic['name'].str.split(',',expand=True)[0]
print("The number of unique surnames in the dataset is {}".format(titanic['surname'].nunique()))