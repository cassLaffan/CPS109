import math
# Let's find an arbitrary root for any number!

if __name__ == "__main__":
    # Type safety? Never heard of her.
    # Let's say I left this in as an example of nested type conversion
    num = float(abs(int(input("What number do you want the root for?\n"))))
    root = float(abs(int(input("And what root do you want to find for it?\n"))))

    lo = 0
    hi = max(num, 1.0)

    guess = (lo + hi) / 2
    epsilon = 0.001
    error = guess ** root - num

    # So for those who are confused by this (I ripped it out of the p. 33 in the textbook)
    # Think of this while loop like a pendulum, with the root specified above
    # as the centre. The program will swing back and forth past the real root,
    # adjusting its swing, until eventually it lands approximately in the centre.
    # (On the root).
    while abs(error) > epsilon :
        if error < 0 :
            lo = guess
        else :
            hi = guess

        guess = (lo + hi) / 2
        error = guess ** root - num

    print('The approximate cube root of ', num, 'is', guess)
