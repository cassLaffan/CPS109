
'''
Prompts the user for keys, then values.
'''
def make_dict():
    inp = ""
    # Syntax for creating a dictionary!
    # Notice the squiggly brackets.

    our_dict = {}
    while inp != "Stop!":
        inp = input("Please enter a store: ")
        inp_prod = input("Now please enter what product they sell: ")
        # Creates a key and associated value
        our_dict[inp] = inp_prod
        inp = input("Would you like to continue? Type 'Stop!' to stop. ")

    return our_dict

if __name__ == "__main__":
    print(make_dict())
    print("Goodbye!")