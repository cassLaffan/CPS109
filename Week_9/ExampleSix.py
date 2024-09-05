import random

def print_funny(choice):
    our_weird_strings = ["----------", "+++++++++", "+_+_+_+_+_+_+_+_+_+_"]

    for i in choice:
        print(random.choice(our_weird_strings) + i)

if __name__ == "__main__":
    ls = random.randint(0, 10)
    choice_list = []
    for i in range(ls):
        choice_list.append("a" * i)
    
    print_funny(random.choice(choice_list))