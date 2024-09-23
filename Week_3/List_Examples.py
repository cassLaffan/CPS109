'''
Here, we're messing with list functions built into Python!
'''

if __name__ == "__main__":
    # Create an initial list
    my_list = [1, 2, 3]
    print("Initial list:", my_list)

    # Append a value to the end
    my_list.append(4)
    print("After appending 4:", my_list)

    # Extend a list by the following elements
    my_list.extend([5, 6, 7])
    print("After extending with [5, 6, 7]:", my_list)

    # Insert 14 at the beginning
    my_list.insert(0, 14)
    print("After inserting 14 at index 0:", my_list)

    # Remove the first occurrence of 3
    my_list.remove(3) 
    print("After removing 3:", my_list)

    # Remove and return the last item
    popped_item = my_list.pop() 
    print("Popped item:", popped_item)
    print("After popping the last item:", my_list)

