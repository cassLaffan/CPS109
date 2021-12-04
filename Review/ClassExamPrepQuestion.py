import unittest

'''
Completing this class rundown should mean that you are pretty well-prepared for the
upcoming exam questions (or at least most of them) on classes.

Generally, concepts you should be familiar with are:
	1. Creating an "__init__" method for your class
		(Including how to make default variables within your class)
	2. Accessing, modifying, and defining variables in the class
	3. Creating instance methods within your class
	4. How to use helper methods alongside classes

This question will get you to do all of the above, and I'll identify the relevant
sections so you can practice what you need specifically. I'll also be going over
the solution to this during the Review Session on Sunday December 5th at 10 am,
and I'll post the solutions on the Discord too!
'''

'''
Story: The Teletubbies are vanquished, but in the realm of dreams they still haunt
you! Your task is to implement the following classes and helper methods according
to the requirements described in each class/method, so as to conquer your nightmares,
and obliterate all traces of the Teletubbies!
'''

class Dream:
	'''
	Dreams are pretty good. Usually with apple pies and candies and all that good stuff.

	Your task is as follows:
	Construct the "__init__" method for a Dream class, that takes in 2 arguments (plus self),
	self (which you ALWAYS require in your constructors, even if there is nothing else in them!)
	a string "title", and
	an int "length"
	And sets a list dream_elements to start as the empty list: []
	[1]

	Then, once you have completed your constructor, create an instance method called
	change_title(a), which changes the title of your dream instance to the string a.
	[2, 3]

	Then, create another instance method called add_to_dream(topic), which adds the string
	topic to the dream_elements list.
	[2, 3]

	Finally, create an instance method dreams_to_dust(), which replaces each element of the 
	dream_elements list with the string "dust".
	[2, 3]
	'''
	pass

class Nightmare:
	'''
	Nightmares are pretty bad. Usually with Teletubbies and chainsaws and all that bad stuff.

	Your task is as follows:
	Construct the "__init__" method for a Nightmare class, that takes in 0 arguments (except self of course)!
	However, you should create an instance variable "topic" that defaults to the string
	"Teletubbies", and an instance variable for an attached Dream that the nightmare is
	in, called "attached_dream" (which defaults to None).
	[1]

	Then, create a method attach_to_dream(d), which attached your nightmare instance
	to a dream via setting attached_dream to the argument Dream d.
	[2, 3]

	Then, create a method has_attached_dream() which returns True if your attached_dream 
	is not None, and False otherwise.
	[2, 3]

	Finally, create a method WAKE_ME_UP(), which will set the attached_dream's length to 0,
	and call it's dreams_to_dust() method.
	[2, 3]
	'''
	pass

def return_titles(list_of_dreams):
	'''
	Create a method that takes in a list of Dreams "list_of_dreams" as input, and returns
	a list containing the titles of all Dreams in that list.
	[2, 4]
	'''
	pass

def WAKE_ME_UP_INSIDE(cant_wake_up):
	'''
	Create a method that takes in a list of Nightmares "cant_wake_up", as input, which
	then calls the WAKE_ME_UP() method for each Nightmare in the list.
	[3, 4]
	'''
	pass

def how_long_are_my_dreams(list_of_dreams):
	'''
	Create a method that takes in a list of Dreams "list of dreams" as input, and returns
	the sum of all Dream lengths in that list.
	[2, 4]
	'''
	pass

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self): # Testing Dream constructor
    	d = Dream("my awesome dream", 5)
    	self.assertEqual(d.title, "my awesome dream")
    	self.assertEqual(d.length, 5)
    	self.assertEqual(d.dream_elements, [])
    def test2(self): # Testing nightmare constructor
    	n = Nightmare()
    	self.assertEqual(n.topic, "Teletubbies")
    	self.assertEqual(n.attached_dream, None)
    def test3(self): # Testing Dream.change_title()
    	d = Dream("my awesome dream", 5)
    	d.change_title("my great dream")
    	self.assertEqual(d.title, "my great dream")
    def test4(self): # Testing Dream.add_to_dream()
    	d = Dream("my awesome dream", 5)
    	d.change_title("my great dream")
    	d.add_to_dream("rainbows")
    	d.add_to_dream("butterflies")
    	self.assertEqual(d.dream_elements, ["rainbows", "butterflies"])
    def test5(self): # Testing Dream.dreams_to_dust()
    	d = Dream("my ruined dream", 5)
    	d.add_to_dream("rainbows")
    	d.add_to_dream("butterflies")
    	d.add_to_dream("horsies")
    	d.dreams_to_dust()
    	self.assertEqual(d.dream_elements, ["dust", "dust", "dust"])
    def test6(self): # Testing Nightmare.attach_to_dream()
    	n = Nightmare()
    	d = Dream("my awesome dream", 5)
    	n.attach_to_dream(d)
    	self.assertEqual(n.attached_dream, d)
    def test7(self):
    	n = Nightmare()
    	d = Dream("my awesome dream", 5)
    	self.assertEqual(n.has_attached_dream(), False)
    	n.attach_to_dream(d)
    	self.assertEqual(n.has_attached_dream(), True)
    def test8(self): # Testing Nightmare.WAKE_ME_UP()
    	n = Nightmare()
    	d = Dream("my awesome dream", 5)
    	d.add_to_dream("pumpkins")
    	n.attach_to_dream(d)
    	n.WAKE_ME_UP()
    	self.assertEqual(d.length, 0)
    	self.assertEqual(d.dream_elements, ["dust"])
    def test9(self): # Testing return_titles()
    	d1 = Dream("my awesome dream!", 5)
    	d2 = Dream("my fantastic dream!!", 4)
    	d3 = Dream("my superb dream!!!", 3)
    	self.assertEqual(return_titles([d1, d2, d3]), ["my awesome dream!", "my fantastic dream!!", "my superb dream!!!"])
    def test10(self): # Testing WAKE_ME_UP_INSIDE()
    	d1 = Dream("my awesome dream!", 5)
    	d1.add_to_dream("sprinkles")
    	d2 = Dream("my fantastic dream!!", 4)
    	d2.add_to_dream("cake")
    	d2.add_to_dream("chocolates")
    	n1 = Nightmare()
    	n2 = Nightmare()
    	n1.attach_to_dream(d1)
    	n2.attach_to_dream(d2)
    	WAKE_ME_UP_INSIDE([n1, n2])
    	self.assertEqual(d1.length, 0)
    	self.assertEqual(d2.length, 0)
    	self.assertEqual(d1.dream_elements, ["dust"])
    	self.assertEqual(d2.dream_elements, ["dust", "dust"])
    def test11(self): # Testing how_long_are_my_dreams()
    	d1 = Dream("my awesome dream!", 5)
    	d2 = Dream("my fantastic dream!!", 4)
    	d3 = Dream("my superb dream!!!", 3)
    	self.assertEqual(how_long_are_my_dreams([d1, d2, d3]), 12)
if __name__ == '__main__':
 unittest.main(exit=True)
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
