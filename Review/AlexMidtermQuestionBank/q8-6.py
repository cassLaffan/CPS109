import unittest

def marketResearch(carts):
    '''
    Assume carts is a list of of lists that represent items that users have purchased

    For example:
    [['peas','potatoes','gravy','chicken'],['potatoes','gravy','beans','steak'],['potatoes','grapes'],['grapes','steak','beans']]

    Return a tuple of the most commonly purchased item, and the item that most commonly appears in lists that contain the most common tiem.

    For example, potatoes is the most common item across the lists.
    Among the lists containing potatoes, gravy is the most common item (excluding potatoes).

    Therefore we return (potatoes, gravy)
    '''
    pass


class marketResearchTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(marketResearch([['peas','potatoes','gravy','chicken'],['potatoes','gravy','beans','steak'],['potatoes','grapes'],['grapes','steak','beans']]), ('potatoes', 'gravy'))
    def test2(self):
        self.assertEqual(marketResearch([['rgb fans','cpu','graphics card'],['graphics card','rgb fans'],['cpu','monitor'],['graphics card']]), ('graphics card', 'rgb fans'))
    def test3(self):
        self.assertEqual(marketResearch([['rice','black beans'],['rice','water','fanta'],['rice','black beans','sprite'],[]]), ('rice','black beans'))
    def test4(self):
        self.assertEqual(marketResearch([['rice','black beans'],['rice','splenda'],['rice'],['splenda']]), ('rice','black beans'))
    def test5(self):
        self.assertEqual(marketResearch([['grapes','squash'],['squash']]), ('squash','grapes'))

if __name__ == '__main__':
    unittest.main(exit=True)