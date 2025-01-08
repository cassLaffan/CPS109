import random

if __name__ == "__main__":
    # Seed, using the default
    random.seed()

    # Random integers
    print(random.randint(1, 6))  # Simulates rolling a die
    print(random.randrange(0, 100, 10))  # Random number in steps of 10

    # Shuffling a list
    my_list = [1, 2, 3, 4, 5]
    random.shuffle(my_list)
    print(my_list)  # Outputs a shuffled list, e.g., [3, 1, 4, 2, 5]
