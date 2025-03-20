import pandas

if __name__ == "__main__":
	df = pandas.DataFrame({'X' : ['B', 'B', 'A', 'A'], 'Y' : [1, 2, 3, 4]})
	print(df)
	# Group by operations
	print(df.groupby(['X']).sum())
	# Outdated, someone should tell the head prof!
	print(df.groupby(['X']).get_group('A'))

	# Pivot tables
	pv = pandas.pivot_table(df, index=["X"], aggfunc='sum')
	print(pv)