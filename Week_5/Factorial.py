# Let's do a recursive function that calculates a factorial!

def factorial(num):
    new_num = 0
    # Base case is num == 0
    if(num < 1):
        new_num = 1
    else:
       new_num = num * factorial(num - 1)
    return new_num

if __name__ == "__main__":
    print(f"{5}! = {factorial(5)}")