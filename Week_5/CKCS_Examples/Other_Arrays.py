import numpy

if __name__ == "__main__":
	# Linspace will create an array with the number of indicies equally spaced
	# between the first and second numbers
	print(numpy.linspace(0, 25, 10))

	# Similar to the range function, but makes an array
	print(numpy.arange(1, 11, 1))

	# Will create a matrix with mostly 0s, with whatever number you enter
	# interrupting in a diagnal fashion
	diagn = numpy.diag([3, 3, 3, 3])

	# Will create a matrix of only zeros (in float format)
	print(numpy.zeros(10))

	# Will create a matrix of ones (also in float format)
	ones = numpy.ones((4, 4))

	print(ones * 4)
	print(diagn * 5)

	numpy.random.seed()

	print(numpy.random.rand(3, 3))

	#ones.shape = (-1, 1)

	print(diagn)
	print(diagn.transpose())

	print(numpy.linalg.inv(diagn))

	print(ones)
	print(numpy.dot(ones, diagn))
	print(numpy.eye(3))

	# Are actually looking at the same block of memory for the same matrix
	new_ones = ones
	print(ones is new_ones)
	# Allocates a new block of memory and copies all of the values over
	second_new_ones = new_ones.copy()
	print(new_ones is second_new_ones)

	print(ones.var())
	print(ones.std())
