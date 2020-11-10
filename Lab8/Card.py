class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

def createDeck():
    colors = ['heart', 'diamonds', 'spades', 'clubs']
    nums = [Card(value, color) for value in range(1, 11) for color in colors]
    face = [Card(10, color) for value in range(0, 3) for color in colors]
    nums.extend(face)

    return nums
