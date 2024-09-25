'''
This program will implement a conditional stop light.
'''

def stop_colour(light):
    if light.lower() == "red":
        print("Stop!")
    elif light.lower() == "yellow":
        print("Slow down!")
    elif light.lower() == "green":
        print("Go!")
    else:
        print("Invalid light colour, contact the city.")

if __name__ == '__main__':
    user_input = ""

    while user_input.lower() != "end":
        user_input = str(input("What colour is our light? "))
        if user_input.lower() != "end":
            stop_colour(user_input)
    
