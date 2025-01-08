from itertools import islice

if __name__ == "__main__":
    numbers = (x * x for x in range(10))  # Lazy generator
    squared_numbers = list(islice(numbers, 3))  # Get first 3 squares
    print(squared_numbers)  # Outputs: [0, 1, 4]

