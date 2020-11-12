class Card:
    def __init__(self, value, colour):
        self.value = value
        self.colour = colour

'''
This syntax below is called list comprehension!
What this does puts a loop inside a list.

nums = [Card(value, colour) for value in range(1, 11) for colour in colours]
can be written as:

for value in range(1, 11):
    for colour in colours:
        nums.append(Card(value, colour))

See? It makes an object then appends it to the list!
'''
def createDeck():
    colours = ['heart', 'diamonds', 'spades', 'clubs']
    nums = [Card(value, colour) for value in range(1, 11) for colour in colours]
    face = [Card(10, colour) for value in range(0, 3) for colour in colours]
    nums.extend(face)

    return nums
