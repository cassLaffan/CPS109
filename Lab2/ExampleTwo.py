# I would label these files with more meaningful names but then
# you wouldn't read through all of them :P

# This example shows us two things
# First, how a for loop would iterate over not one, but two strings.
# It also shows us a nested for loop, as in, theres a for loop inside a for loop.
# Notice how in the second for loop, it still knows what value i is?
# i is local to the top most for loop. Once that outer loop is terminated,
# then it will no longer know what i is.
if __name__ == "__main__":
    strOne = "Gibberish?"
    strTwo = "Perish the thought!"

    for i in strOne:
        for j in strTwo:
            print(i + j, end = '')
