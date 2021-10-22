# Let's do a recursive function that calculates a factorial!

def factorial(num):
# Base case is num == 0
   if(num < 1):
       print("We have reached 0!")
       return 1
   else:
       new_num = num * factorial(num - 1)
       print("Our current factorial value is: ", new_num)
       return new_num

if __name__ == "__main__":
    print("{}! = {}".format(5, factorial(5)))