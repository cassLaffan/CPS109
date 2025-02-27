import numpy

if __name__ == "__main__":
	an_array = numpy.array([33, 44, 10, 40])
	second_array = numpy.array([5, 1, 7, 10])

	print(an_array)
	vec = an_array + second_array
	print(vec)
	print(type(an_array))
	print(type(vec))

	print(vec.shape)
	print(vec.dtype)
