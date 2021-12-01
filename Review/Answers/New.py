'''
Write a RECURSIVE function that performs the same
functionality as the function in Brackets.py.
'''

def find_balance(s, r = 0, l = 0):
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
        if r == abs(l):
            check = True
        else:
            check = False
    elif len(s) == 1:
        if s[0] == "}" and r == 1:
            check = True
        elif s[0] == "{" and l == -1:
            check = True
        else:
            check = False
    elif len(s) == 2:
        if s == "{}":
            check = True
        elif s == "}{" and r == 1 and l == -1:
            check = True
        else:
            check = False

    # Now the recursive step.
    else:
        if s[0] == "{":
            r += 1
        if  s[-1] == "}":
            l -= 1
        
        check = True and find_balance(s[r:l])

    return check
'''
Note: There are no tests included in this file. Use the
tests you've written in CreateTest.py to test your code.
'''