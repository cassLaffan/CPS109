'''Second bad coding example.'''

# This program will work but there are many things wrong with it.

# Two problems arise here: first, a and b are sitting in the ether.
# Second, there are typos in the strings. Proof read your code!
# Just because Python doesn't complain about your spelling inside of
# strings doesn't mean you should write garbage.
a = input("iunput string:")
b = input("inpoot strung:")

# Several problems arise from this func definition. First, it is named
# ambigiously so the reader has no idea what they're looking at.
# Second, there are function definitions within the function.
# Having functions declared in functions won't necessarily throw an error
# but it indicates that you have no idea why functions are used.
# Third, I am calling a and b inside of these functions which are declared
# outside of any code blocks, at the beginning of the code. These are essentially
# globals without the 'global' keyword.
def func():
    def func_two(a):
        print(a)
    def func_three(b):
        print(b)
    func_two()
    func_three()

# If you open this inside of your code editor (which you should), you'll
# see that these function calls are underlined in red. That's because these
# functions are declared locally inside of func() and when you try to run this
# code, you'll get an error.
func_two(a)
func_three(b)