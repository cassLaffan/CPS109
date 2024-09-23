'''
Here, we're exploring how we can nest logic,
even, loops, inside a while loop.
'''

if __name__ == '__main__':
    i = 1
    while i <= 5:
        j = 1
        while j <= 5:
            print("Our new product is: ", i * j)
            j += 1
        i += 1