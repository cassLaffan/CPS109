import unittest
import Brackets

'''
For this question, assume you have a function called find_balance
from a seperate module called Brackets. This function takes one 
argument, a string of 0 or more brackets, such as "}}{{}{}" or
"}}}{{{" or "{}{}{}{}". It will access whether or not a string of
these brackets is balanced or not. If a string IS balanced, it will
return True. If it IS NOT balanced, it will return False.

A string is considered balanced if it is empty, if it is of the form
{}, or it is of the form {x}, where x is also a balanced string. It is
also balanced if it is of the form {x}{x}, where x is either empty, or
contains other balanced strings. So, for example,

Brackets.find_balance("{{}}") -> True
Brackets.find_balance("}{") -> False

Write FIVE test cases for this function, including two that account for
abnormal (edge) cases. Do not include the two examples above.

To call this function, you will use the syntax Brackets.find_balance(argument).
'''

class BracketTest(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main(exit=True)