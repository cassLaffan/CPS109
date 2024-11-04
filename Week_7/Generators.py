'''

'''

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

if __name__ == "__main__":
    counter = count_up_to(5)
    for num in counter:
        print(num)  # Outputs: 1, 2, 3, 4, 5