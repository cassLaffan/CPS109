'''
def first_preceded_by_smaller(items, k=1):

Find and return the first element of the given list of items 
that is preceded by at least k smaller elements in the list. 
These required k smaller elements can be positioned anywhere 
before the current element, not necessarily consecutively 
immediately before that element. 

If no element satisfying this requirement exists anywhere in 
the list, this function should return None.

Since the only operation performed for the individual 
items is their order comparison, and especially no arithmetic 
occurs at any point during the execution, this function should 
work for lists of any types of elements, as long as those 
elements are pairwise order comparable with each other.
'''

def first_preceded_by_smaller(items, k=1):
    count_value = 0
    return_value = None

    for i in range(k, len(items)):
        count_value = 0
        for j in range(i):
            if(items[j] < items[i]):
                count_value += 1
        if(count_value >= k):
            return_value = items[i]
            break

    return return_value

if __name__ == "__main__":
    lst = [4, 4, 5, 6]
    print(first_preceded_by_smaller(lst, 2))

    lst_new = [42, 99, 16, 55, 7, 32, 17, 18, 73]
    print(first_preceded_by_smaller(lst_new, 3))

    lst_string = ['bob', 'carol', 'tina', 'alex', 'jack', 'emmy', 'tammy', 'sam', 'ted']
    print(first_preceded_by_smaller(lst_string, 4))

    long_lst = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]
    print(first_preceded_by_smaller(long_lst))
