'''
Write a RECURSIVE function that performs the same
functionality as the function in Brackets.py.
'''

def find_balance(s):
    '''
    Takes a string of brackets as an argument. Will return
    True or False, depending on whether or not the string 
    is balanced. An empty string is balanced.

    find_balance("}}}{") -> False
    find_balance("{}{}") -> True
    '''
    check = False

    # Lots of base cases in this instance.
    if len(s) == 0:
        check = True
    elif len(s) == 2:
        if s == "{}":
            check = True
        else:
            check = False
    # This is here just for completion purposes, can easily be skipped
    elif len(s)%2 == 1:
        check = False

    # Now the recursive step.
    else:
        if s[0] != "{" and s[-1] != "}":
           check = False
        else:
            check = True and find_balance(s[1:-1])

    return check
'''
Note: There are no tests included in this file. Use the
tests you've written in CreateTest.py to test your code.
'''