# Let's do a basic example of exhaustive enumeration
# (also known as brute force!) through a very basic list.


# What this function will do is take two arguments:
# First, a list, then the integer you want to find in the list
# it will return a list of the indicies where new_num occurs.
def check_every_item(my_list, new_num):

    # Let's define an empty list that we can append our indicies to.
    ind_list = []

    i = 0

    while i < len(my_list):
        if my_list[i] == new_num:
            # Lists, unlike strings, can be modified!
            # So we just add new items to it.
            ind_list.append(i)
        i+=1

    return ind_list

if __name__ == "__main__":
    # Here we will define a list in our program.
    # We will have some examples later on that will have more
    # dynamic lists made from user input.

    # The numbers are intentional
    new_list = [2, 5, 1, 6, 2, 82, -10, 2]

    index_list = check_every_item(new_list, 2)

    # The output for this program will be [0, 4, 7]
    # Meaning we had to iterate through every single element to find every 2.
    print(index_list)