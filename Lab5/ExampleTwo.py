# Let's do a recursive function that calculates a factorial!

def factorial(num):
   if(num < 1):
       return 1
   else:
       new_num = num * factorial( num - 1 )  # recursive call
       return new_num

if __name__ == "__main__":
    print("{}! = {}".format(4, factorial(4)))