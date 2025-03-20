import pandas as pd

if __name__ == "__main__":
	s1 = pd.Series(['a', 'b'])
	s2 = pd.Series(['c', 'd'])
	print(pd.concat([s1, s2]))
