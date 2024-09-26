'''
Here, we will examine the range function and its
various arguments!
'''

if __name__ == "__main__":
    # range can have two arguments: start, stop
    for i in range(2, 6):
        print(i)

    # range can also have three arguments: start, stop, step
    # step is how you're counting up from start to stop
    for i in range(0, 10, 2):
        print(i)

    # You can also use step and a bigger start, smaller stop
    # to step backwards!
    for i in range(5, 0, -1):
        print(i)

