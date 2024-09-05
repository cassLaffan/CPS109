import random

'''
Let's use random to create a miltidimensional array (list)
'''
if __name__ == "__main__":
    # This is necessary. You can't get random numbers
    # without seeding it first
    random.seed()

    our_dimension = random.randint(0, 10)
    our_matrix = []

    # It's really just nested lists, I promise
    for d in range(our_dimension):
        our_matrix.append([])
        for i in range(our_dimension):
            our_matrix[-1].append(random.randint(-10, 10))
        print(our_matrix[-1])

    print(our_matrix)