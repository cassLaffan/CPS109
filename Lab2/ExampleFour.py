# Now let's look at while loops

# This is a very simple example of a while loop
# How a while loop works is that it will loop for every time its condition isn't
# found to be true. In this case, it will loop once more every time it finds that x 
# is strictly less than 10. Once x == 10, then it will no longer execute any of the 
# code within the loop.
if __name__ == "__main__":
    x = 0

    while x < 10:
        print(x)
        x+=1