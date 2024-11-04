import unittest
import Week_7.Car_Class as Car_Class

class my_tests(unittest.TestCase):
    def test1(self):
        car_one = Car_Class.car("Honda Civic", "Red", 14000)
        car_two = Car_Class.car("Toyota RAV4", "Green", 14000)
        self.assertEqual(Car_Class.compare_price(car_one, car_two), True)
    def test2(self):
        car_three = Car_Class.car("Chrysler Malibu", "Blue", 9000)
        car_one = Car_Class.car("Honda Civic", "Red", 14000)
        self.assertNotEqual(Car_Class.compare_price(car_one, car_three), True)

if __name__ == '__main__':
    unittest.main(exit=True)