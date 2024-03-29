import unittest
'''This class represents a rectangle in the x-y coordincate system
where the edges of the rectangle are aligned with the x- and y- axes.
A Rectangle object has data attributes lowerleft and upperright,
which are tuples representing the (x, y) coordinates of the lower 
left corner and the upper right corner.

Fill in functions for the class.
'''

class Rectangle(object):
    def __init__(self, x1, y1, x2, y2) :
        '''Assumes the (x1, y1) are the coordinates of the lower left corner
        and (x2, y2) are the coordinates of the upper right corner.
        '''
        self.lowerleft = (x1, y1)
        self.upperright = (x2, y2)

    def width(self) :
        '''Returns the width of the rectangle
        '''
        return self.upperright[0] - self.lowerleft[0]

    def height(self) :
        '''Returns the height of the rectangle
        '''
        return self.upperright[1] - self.lowerleft[1]
    
    def area(self) :
        '''Returns the area of the rectangle'''
        return self.height() * self.width()

    def __eq__(self, other) :
        '''Returns true if the two rectangles have equal area'''
        return self.area() == other.area()

class RecTests(unittest.TestCase):
    def test1(self):
        box1 = Rectangle(0, 0, 2, 2)
        self.assertEqual(box1.width(), 2)
    def test2(self):
        box1 = Rectangle(0, 0, 2, 2)
        self.assertEqual(box1.height(), 2)
    def test3(self):
        box1 = Rectangle(0, 0, 2, 2)
        self.assertEqual(box1.area(), 4)
    def test4(self):
        box1 = Rectangle(0, 0, 2, 2)
        box2 = Rectangle(2, 2, 6, 3)
        self.assertTrue(box1 == box2)

if __name__=='__main__':
    unittest.main(exit=True)
