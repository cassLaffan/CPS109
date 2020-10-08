# Let's program a factorial.
# Remember: a factorial is just that number multiplied
# by every single number in the range of it and 1.
# Like, 4! = 4 * 3 * 2 * 1 = 24

def factorial(num):
    fact_num = 1

    for i in range(1, num + 1):
        fact_num = fact_num * i

    return fact_num

if __name__ == "__main__":
    inp = input("What number should we calculate the factorial for?\n")

    print(factorial(int(inp)))