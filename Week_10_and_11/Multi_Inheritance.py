class Animal:
    def speak(self):
        print("Animal speaks")

class Bird:
    def fly(self):
        print("Bird is flying")

class FlyingAnimal(Animal, Bird):
    pass

if __name__ == "__main__":
    fa = FlyingAnimal()
    fa.speak()  # Inherited from Animal
    fa.fly()    # Inherited from Bird
