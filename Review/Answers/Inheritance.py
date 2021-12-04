class Animal:
    '''
    An implementation of the Animal parent class.
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return (self.name == other.name) and (self.age == other.age)

    def take_for_walk(self):
        print(f"Your {self.name} has gone for a walk!")

class Cat(Animal):
    '''
    Child class of Animal called Cat. Since cats aren't
    brushed by default, the member variable for is_brushed is
    set to False.
    '''
    def __init__(self, name, age, fur_colour, eye_colour):
        # This is the idiomatic way to call the parent class' constructor
        super().__init__(name, age)
        # Since is_brushed is automatically False, I have opted to not have it as an argument
        # in the constructor.
        self.fur_colour = fur_colour
        self.eye_colour = eye_colour
        self.is_brushed = False
    
    def __eq__(self, other):
        return (super().__eq__(other)) and (self.eye_colour and other.eye_colour) and (self.fur_colour and other.fur_colour) and (self.is_brushed and other.is_brushed)
    
    def brushie(self):
        self.is_brushed = True
        print(f"{self.name} has been brushed! (^._.^)")

if __name__ == "__main__":
    '''
    Make two Cat objects in the main and call your member
    method for Brushies on one. Then, compare them and print the
    result.
    '''
    mischief = Cat("Mischief", 13, "Brown", "Green")
    chaos = Cat("Chaos", 11, "Grey and white", "Yellow/Green")

    mischief.brushie()

    print(mischief == chaos)