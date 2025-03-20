import pandas

def times_two(x):
	return x * 2

if __name__ == "__main__":
	# A dictionary containing some data!
	data = {'Company':['Cmp 1', 'Cmp 1', 'Cmp 2', 'Cmp 2', 'Cmp 3','Cmp 3'],
		 'Person':['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
		 'Sales':[200,0,340,124,0,350]}
	
	# Creating a data frame based off the data
	df = pandas.DataFrame(data)

	print(df)

	# Comparator with the numerical value!
	print((df.Sales > 200)) # Gives you a new table of each comparison
	print(df[df.Sales > 0]) # Will give you a table of the rows that match the condition
	
	# This works because times_two is a function object
	print(df.Sales.apply(times_two))

	df.loc[df.Sales == 0, 'Sales_times_2'] = 200

	print(df)

	# Checks if a Person contains a certian substring
	print(df[df.Person.str.contains('am', case=True)])