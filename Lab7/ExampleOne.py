def mostfrequent(L) :
    '''
    Assume that L is a non-empty list.
    Return the number which is most frequent in the list.
    For example, 
    mostfrequent([5, 2, 9, 2, 9, 1, 18, 9, 3]) would return 9, since 
    there are three 9's, and two 2's, and one of other values.
    '''
    maximum = 0
    maximum_count = 1

    for i in L:
        temp_count = 0
        for j in L:
            if i == j:
                temp_count =  temp_count + 1
        if temp_count >= maximum_count:
            maximum = i
            maximum_count = temp_count

    return maximum

if __name__ == "__main__":
    print(mostfrequent([5, 2, 9, 2, 9, 1, 18, 9, 3]))