'''
This program will implement a conditional stop light.
'''

def stop_colour(light):
    if light == "Red" or light == "red":
        print("Stop!")
    elif light == "Yellow" or light == "yellow":
        print("Slow down!")
    elif light == "Green" or light == "green":
        print("Go!")
    else:
        print("Invalid light colour, contact the city.")

if __name__ == '__main__':
    inp_one = input("What colour is our light? ")
    stop_colour(inp_one)
    inp_one = input("Now what is the light colour? ")
    stop_colour(inp_one)
    inp_one = input("What is the colour now? ")
    stop_colour(inp_one)

    
