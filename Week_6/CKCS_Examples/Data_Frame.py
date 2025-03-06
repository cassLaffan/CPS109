import pandas as pd
import numpy as np
from IPython.display import display
from numpy.random import randn

if __name__ == "__main__":
	np.random.seed(101)
	new_data_frame = pd.DataFrame(randn(5,4),index=['A', 'B', 'C', 'D', 'E'],columns=['W', 'X', 'Y', 'Z'])
	print(new_data_frame)

	print(new_data_frame['W'])
	# Will access columns
	print(new_data_frame[['W', 'Z']])
	# Will access rows
	print(new_data_frame[0:2])
	# Short for index location
	print(new_data_frame.iloc[3])
	# Short for location
	print(new_data_frame.loc['A'])

	# Adding a column
	new_data_frame['R'] = new_data_frame['W'] + new_data_frame['Y']
	print(new_data_frame)
	# Removing a column, inplace is necessary
	new_data_frame.drop('R', axis=1, inplace=True)
	print(new_data_frame)
	# Remove row, inplace tells Python we are certian!
	new_data_frame.drop('C', axis=0, inplace=True)
	print(new_data_frame)

	# Needs square brackets
	# NaN means Not a Number!
	print(new_data_frame[new_data_frame < 0])

	# Will fetch the first n rows (the head of the spreadsheet)
	print(new_data_frame.head(2))
	# Will give you the unique entries in a column
	print(new_data_frame['W'].unique())
	# Will give you a randomly ordered sample from your data frame
	print(new_data_frame.sample(3))

	# Regex is short for regular expression and it is a pattern matching
	# syntax.
	print(new_data_frame.filter(regex='1|2',axis=1))
	print(new_data_frame.filter(regex='1|2',axis=0))
	# Will give you information
	print(new_data_frame.info())
	# Will give you the mathematical information
	print(new_data_frame.describe())

	print(new_data_frame.sort_values(by='W'))

	display(new_data_frame)