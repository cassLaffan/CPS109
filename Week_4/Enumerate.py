'''
In this file, we will be using enumeration to navigate
lists!
'''

if __name__ == "__main__":
    # I like fruit ok
    fruits = ['strawberry', 'blueberry', 'cherry']

    for index, fruit in enumerate(fruits):
        print(f"Index {index}: {fruit}")

    # You can also decide what index you wish to start at
    # using the start argument
    for index, fruit in enumerate(fruits, start=1):
        print(f"Fruit number {index}: {fruit}")
