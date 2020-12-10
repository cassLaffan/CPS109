import unittest

def shopSort(productDict):
    '''
    Assume that productDict is a dictionary of product price pairs
    
    EX:
    {
        'rice':10.99
        'cheese':3.99
        'eggs':5.99
    }

    Return a list of tuples of all the products in the dict 
    sorted by price from greatest to least.

    For example, the above dictionary would return:

    [('rice',10.99), ('eggs',5.99), ('cheese',3.99)]
    '''
    pass

class shopSortTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(shopSort({'rice':10.99,'cheese':3.99,'eggs':5.99}),
        [('rice',10.99), ('eggs',5.99), ('cheese',3.99)])
    def test2(self):
        self.assertEqual(shopSort({'water':2.99,'gum':1.50,'burger':5.99,'crackers':3.00}),
        [('burger',5.99), ('crackers',3.00),('water',2.99), ('gum',1.50)])
    def test3(self):
        self.assertEqual(shopSort({'cola':2.00,'redbull':3.49}),
        [('redbull',3.49),('cola',2.00)])
    def test4(self):
        self.assertEqual(shopSort({'kool aid':15.00,'grape juice':100.22,'Q-tip':1000.39}),
        [('Q-tip',1000.39),('grape juice',100.22),('kool aid',15.00)])
    def test5(self):
        self.assertEqual(shopSort({'these':100,'all':100,'have':100,'the':100,'same':100,'price':100}), 
        [('these',100),('all',100),('have',100),('the',100),('same',100),('price',100)])

if __name__ == '__main__':
    unittest.main(exit=True)