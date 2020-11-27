
def print_matrix(our_matrix):
    for i in our_matrix:
        for j in i:
            print(" | " + str(j), end="")
        print("| ")

if __name__ == "__main__":
    our_matrix = [[3, 1, 4], [2, 56, 1], [0, 0, 0]]

    print_matrix(our_matrix)

    for i in our_matrix:
        print(i)