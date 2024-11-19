class LangDict:
    '''
    This class is a demonstration of more class syntax,
    as well as containing a dictionary in a class.
    '''

    # Notice that we only have name as an argument for the init function
    # This is to demonstrate that you don't need to initialize with arguments
    # necessarily. You can easily have member variables that weren't fed in as
    # arguments
    def __init__(self, name):
        self.name = name
        self.lang_dict = {}
    
    def add_dict(self, k, v):
        self.lang_dict[k] = v

    def look_up(self, search):
        # You can check if a key exists in a dictionary with the key word "in"
        if search in self.lang_dict:
            # This is also the syntax for getting a value from a dictionary
            # dictionary[key] -> value
            return self.lang_dict[search]
        else:
            return None

# A menu helper function to make this program run a bit easier.
def menu():
    choice = 0

    while choice != 1 and choice != 2:
        choice = int(input("If you would like to add a key/value pair to the dictionary, press 1. If you would like to search for a key, press 2.\n"))

    return choice

# Main block for this program. We create a dictionary and then enter words and their definitions 
# to it.
if __name__ == "__main__":
    new_dict_class = LangDict(input("Please enter the name of the dictionary.\n"))

    inp = "-1"

    while inp != "":
        option = menu()
        if option == 1:
            k = str(input("Please input a word.\n"))
            v = str(input("Please input its definition.\n"))
            new_dict_class.add_dict(k, v)
        elif option == 2:
            result = new_dict_class.look_up(str(input("What word would you like to look up?\n")))
            if result == None:
                print("Word does not exist in the dictionary! Please add it.")
            else:
                print(str(result))
        inp = str(input("Press 'enter' to exit. Otherwise, enter whatever you want lol.\n"))
