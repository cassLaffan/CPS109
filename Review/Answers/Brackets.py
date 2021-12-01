def find_balance(s):
    '''
    Takes a string of brackets as an argument. Will return
    True or False, depending on whether or not the string 
    is balanced. An empty string is balanced.

    find_balance("}}}{") -> False
    find_balance("{}{}") -> True
    '''
    counter = 0
    for ch in s:
        if ch == "{":
            counter += 1
        else:
            counter -=1
        if counter < 0:
            break

    return counter == 0