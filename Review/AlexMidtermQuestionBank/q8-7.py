import unittest

def primeTime(showDict, viewerList):
    '''
    Assume that showDict is a dictionary containing the names of TV shows and their air times in military time. 
    Also, assume that each show airs for an hour
    
    For example:
    {
        'Nighly News':1800,
        'Really Ancient Aliens':2200,
        'Morning Report':600,
        'Mourning Report':1130
    }

    and that viewerList contains a list of tuples representing the start and stop times of when a user watches their TV

    For example:
    [(600,1230),(1200,1900),(1130,1230)]

    Return the name of the most watched show, assuming that a user 'watches' the show if its air time 
    falls between their start and stop times, and that they watch the show for its full duration of an hour.

    For example:
    User 1 (600,1230) watched 'Morning Report' and, 'Mourning Report' in their entirety
    User 2 (1200,1900) watched 'Nightly News' in its entirety
    User 3 (1130,1230) watched 'Mourning Report' in their entirety

    Because 2 users watched 'Mourning Report' in its entirety, return the function would return 'Mourning Report'
    '''
    pass

class primeTimeTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(primeTime({'Nighly News':1800, 'Really Ancient Aliens':2200, 'Morning Report':600, 'Mourning Report':1130}, [(600,1230),(1200,1900),(1130,1230)]),'Mourning Report')
    def test2(self):
        self.assertEqual(primeTime({'Jazz Nightly':1900, 'Speedy Cars':1200, 'McGruff, Crime Dog':1600, 'Worm Eating Contest':100}, [(100,200),(10,1900),(120,1300),(1200,1700)]),'Speedy Cars')
    def test3(self):
        self.assertEqual(primeTime({'Jazz Nightly':1900, 'Speedy Cars':1200, 'McGruff, Crime Dog':1600, 'Worm Eating Contest':100}, [(100,200),(10,1900),(1230,2000),(1200,2000)]),'McGruff, Crime Dog')
    def test4(self):
        self.assertEqual(primeTime({'3 Billion Devices drinking coffee':1000,'See Sharp, an intro to coding at Microsoft':900, 'Steve Irwin teaches Python':1900}, [(10,200),(10,1800),(900,1000),(900,1999)]),'See Sharp, an intro to coding at Microsoft')
    def test5(self):
        self.assertEqual(primeTime({'Fortnite Pro Series':1800,'How to floss, a tutorial':1200, 'TikTok and you':700, 'How to connect with the youth':500}, [(10,600),(500,800),(1800,1900),(1200,1900)]),'Fortnite Pro Series')


if __name__ == '__main__':
    unittest.main(exit=True)