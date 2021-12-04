'''
Here is the implementation of a parent class called 
Animal. As you can see, it has the constructor (that __init__)
already implemented, as well as a member method. Implement 
the __eq__ method for animal such that Python returns True if
the name and age of both of the animals being compared are identical.

You are to write a child class of Animal called Cat.
Add another member variable to the Cat class called
fur_colour, eye_colour and is_brushed. is_brushed should
be automatically set to False. Add another class function
called brushies. This function will set the is_brushed
member variable to true and print a cat face to the 
screen (^._.^)

Finally, finish the __eq__ function for cat, such that it
also compared the other member variables of self to other.
Make two Cat objects in the main and call your member
method for Brushies on one. Then, compare them and print the
result.
'''

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return (self.name == other.name) and (self.age == other.age)

    def take_for_walk(self):
        print(f"Your {self.name} has gone for a walk!")

'''
Put your cat class here.
'''

if __name__ == "__main__":
    pass