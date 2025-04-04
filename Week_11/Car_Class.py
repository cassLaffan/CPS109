class Vehicle:
    def start_engine(self):
        print("Starting the engine...")

class car(Vehicle):
    '''
    This is a very basic class. All it has is three properties:
    make, colour, price. Why does it have a "self"?
    Well, let's, instead, look at our method.
    '''
    def __init__(self, m, c, p):
        self.make = m
        self.colour = c
        self.price = p
    
    '''
    Notice how we have to call self again? And how there is only
    one argument, and it's self?

    Let's go look at its implementation
    '''

    def age_price(self):
        self.price = self.price - 500

    # Overriding the parent function
    def start_engine(self):
        print("We're starting this engine instead!")

    def __str__(self):
        return f"Car(make='{self.make}', colour='{self.colour}', price={self.price})"

def compare_price(car_one, car_two):
    return car_one.price == car_two.price

if __name__ == "__main__":
    our_car = car("Honda Civic", "Blue", 12000)
    our_car_2 = car("Honda Civic", "Red", 14000)

    # Calling the parent class' function
    our_car.start_engine()
'''
    print(compare_price(our_car, our_car_2))


    Notice how when we call this method, that it has no arguments?
    Well, python actuall reads it as: age_price(our_car) (sorta).
    The "self" is the current object we're dealing with!

    our_car.age_price()
    print("It now costs: " + str(our_car.price))

    our_car.age_price()
    print("It now costs: " + str(our_car.price))
'''