# Let's take example one and change it so that the list is user entered.

def check_every_item(my_list, new_num):

    # Let's define an empty list that we can append our indicies to.
    ind_list = []

    i = 0

    while i < len(my_list):
        if my_list[i] == new_num:
            ind_list.append(i)
        i+=1

    return ind_list

if __name__ == "__main__":

    new_list = []

    inp = 0

    while inp != -1:
        inp = int(input("Enter a number to add to the list:\n"))
        new_list.append(inp)
    
    new_num = int(input("What number do you want to search for?\n"))

    index_list = check_every_item(new_list, new_num)

    print(index_list)