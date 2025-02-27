import numpy
import scipy

if __name__ == "__main__":
	my_matrix = [[5, 10, 15],
			  [40, 20, 30],
			  [2, 4, 6],
			  [-1, -2, -3]]
	
	new_matrix = numpy.array(my_matrix)
	print(new_matrix)
	print(type(new_matrix))
	print(new_matrix.shape)
	print(new_matrix.dtype)
	print(new_matrix[0])
	
	# We're accessing new_matrix[0][1]
	new_matrix[3, 1] = 70
	#print(new_matrix.transpose())
	print(new_matrix)
	print(new_matrix.argmax())
	print(new_matrix.argmin())
	# Will overwrite your original array
	new_matrix.sort()
	print(new_matrix)

	#print(new_matrix[0:2])
	# Prints off everything at index 1
	#print(new_matrix[:,1])
	# Reassigns everything at index 1
	# new_matrix[:,1] = [0, 0, 0, 0]
	# print(new_matrix)

	bool_matrix = new_matrix < 10
	#print(bool_matrix)
	print(new_matrix.sum())
	print(new_matrix.max())
	print(new_matrix.mean())
	print(scipy.stats.mode(new_matrix))