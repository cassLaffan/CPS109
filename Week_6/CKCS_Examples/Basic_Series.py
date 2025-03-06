import pandas as pd
import numpy as np
from IPython.display import display

if __name__ == "__main__":
	# Creating a basic series from a list
	data = [200, 300, 230, 500, 900]
	idx = [x for x in range(1, 6)]
	new_series = pd.Series(data, dtype=float, index=idx)
	print(new_series)
	print(new_series.index)
	print(new_series.values)

	# Creating a basic series from an ndarray
	months = ['Jan','Feb','March','April','May','June','July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
	monthly_data = [x * 10 for x in range(1, 13)]
	data_arr = np.array(monthly_data)
	month_dict = dict()
	print(monthly_data)
	for num in range(0, 12):
		month_dict[months[num]] = monthly_data[num]
	
	month_series = pd.Series(data=data_arr, index=month_dict)
	print(month_series)

	# Accessing things inside various series
	print(month_series['April'])
	print(new_series[2])
	print(month_series.April)
	print(month_series[5::2])
	print(new_series + month_series)

	display(new_series)