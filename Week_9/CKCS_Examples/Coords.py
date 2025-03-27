# Final exercise, let's open up the coordinates .txt file and plot it!
import matplotlib.pyplot as plt

if __name__ == "__main__":
	x_coords = []
	y_coords = []

	# Opening our file in read mode
	coord_file = open("./coordinates.txt", "r")

	for line in coord_file:
		c_lst = line.split()
		x_coords.append(c_lst[0])
		y_coords.append(c_lst[1])

	coord_file.close()

	plt.plot(x_coords, y_coords, 'g^')
	plt.title("Trend Graph")
	plt.xlabel("Value")
	plt.ylabel("Frequency")
	# Saves the figure to your active directory
	plt.savefig('linechart')
	plt.show()