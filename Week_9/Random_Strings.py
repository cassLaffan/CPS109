import random
'''
Here, we will practice more with the random library. We're taking
a random choice out of an iterable!
'''

def print_funny(choice):
    our_weird_strings = ["----------", "+++++++++", "+_+_+_+_+_+_+_+_+_+_"]

    for i in choice:
        print(random.choice(our_weird_strings) + i)

if __name__ == "__main__":
    random.seed()
    ls = random.randint(0, 10)
    print_funny(random.choice("hello"))