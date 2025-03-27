import matplotlib.pyplot as plt
import numpy as np

'''
Let's plot some graphs! Here we'll use the matplotlib library. To install, type:
python -m pip install -U matplotlib
'''

if __name__ == "__main__":
	# Line graph!
	# Making x,y coords
	xs = [1, 2, 3, 4, 5]
	ys = [x**2 for x in xs]

	# Plotting
	plt.plot(xs, ys)

	# Saving and showing the graph
	# This my take a moment
	plt.savefig('linechart')
	plt.xlabel("Value")
	plt.ylabel("Frequency")
	plt.show()

	# Messing with formatting!
	t = np.arange(0., 5., 0.2)
	plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
	plt.show()

	# Box graph!
	data = [np.random.normal(0, std, 100) for std in range(1, 4)]
	# rectangular box plot
	plt.boxplot(data,vert=True,patch_artist=True)
	plt.show()
