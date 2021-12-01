'''
Write a RECURSIVE function that performs the same
functionality as the function in Brackets.py.

Something of this difficulty will not appear on your
exam. This is just here for fun!
'''

'''
Cassandra's solution logic:

So there are lots of base cases. Instead of working our way
from one side to the other in an iterative fashion, we
work our way into the middle, while keeping a count of the brackets
closed and open on either side of the centre slice.

l (for left) and r (for right) are by default 0. They are what
keep track of the counts on either side.
'''

def find_balance(s, l = 0, r = 0):
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
        if l == abs(r) and l >= 0 and r <= 0:
            check = True
        else:
            check = False
    elif len(s) == 1:
        if s[0] == "}" and l == 1:
            check = True
        elif s[0] == "{" and r == -1:
            check = True
        else:
            check = False
    else:
        if s[0] == "{":
            l += 1
        elif s[0] == "}":
            l -=1
        if  s[-1] == "}":
            r -= 1
        elif s[-1] == "{":
            r += 1
        
        check = True and find_balance(s[1:-1], l, r)

    return check
'''
Note: There are no tests included in this file. Use the
tests you've written in CreateTest.py to test your code.
'''