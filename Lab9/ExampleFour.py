import Card_Class as Card
import random

def draw_card(deck):
    return random.choice(deck)

if __name__ == "__main__":
    random.seed()
    our_deck = Card.createDeck()

    print("Before we draw a random card, our deck contains: " +str(len(our_deck)) + " cards!")

    our_card = draw_card(our_deck)
    if our_card.colour == 'heart':
        our_deck.remove(our_card)
    
    print("How many cards does our deck have now? " + str(len(our_deck)))

    print("Done!")