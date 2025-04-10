# Defining a car class
class Car:
	# Class variable, shared between all cars
	total_cars = 0
	# Initialization function (otherwise known as a constructor)
	def __init__(self, col, pr):
		self.colour = col
		self.price = pr
		Car.total_cars += 1
	
	def __str__(self):
		return f"Car colour: {self.colour}\nCar price: {self.price}"
	
	# Some logic for the + operator.
	# And a type signature, meaning other programmers know that other should be an int
	def __add__(self, other: int):
		self.price += other
	
	def start_engine(self):
		print("Starting engine...")
	
	def drive(self, km):
		self.start_engine()
		print(f"Driving for {km} kilometers.")

	def how_many_cars(self):
		print(Car.total_cars)

if __name__ == "__main__":
	# Calling the constructor
	our_car = Car("Blue", 15000)
	second_car = Car("Red", 100000)

	print(our_car)

	our_car + 300

	print(our_car)

	our_car.drive(100)
	our_car.how_many_cars()