
if __name__ == "__main__":
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']

    result = zip(list1, list2)
    print(list(result))  # Convert iterator to list
