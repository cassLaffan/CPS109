if __name__ == "__main__":
	movies = []
	user_input = str(input("Enter some of your favourite movies! "))
	while user_input.lower() != "exit":
		movies.append(user_input)
		user_input = str(input("Enter another movie. "))

	for i, movie in enumerate(movies):
		print(f"Your number {i + 1} movie is {movie}")