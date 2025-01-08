'''
This is an example of a generator; generators don’t
execute right away. Instead, they return iterator objects.
'''

def count_up_to(n):
    count = 1
    while count <= n:
        print("Hello")
        yield count
        count += 1

def lazy_range(n):
    for i in range(n):
        yield i

def backwards_lazy_range(lower, upper):
    for i in range(upper, lower - 1, -1):
        yield i

if __name__ == "__main__":
    counter = count_up_to(5)
    for num in counter:
        print(num)
    '''
    for num in lazy_range(5):  # Generates numbers 0 to 4 on-demand
        print(num)
    '''

    upper = int(input("What is the upper limit? "))
    lower = int(input("What is the lower limit? "))

    lr = backwards_lazy_range(lower, upper)

    for item in lr:
        print(item)