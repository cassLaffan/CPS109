# This works because dictionaries are mutable.
# Mutable data types are changed in function calls
# and those changes persist because everything in python
# is "Pass by reference".
def memoized_fib(n, memo={}):
    # the memo={} syntax is a default argument
    if n in memo:
        return memo[n]
    elif n <= 1:
        return n
    else:
        # Creating a key-value pair for our dictionary and
        # also passing it along to our two recursive calls.
        # That way, we can persist results across function calls.
        memo[n] = memoized_fib(n - 1, memo) + memoized_fib(n - 2, memo)
        return memo[n]


if __name__ == "__main__":
    print(memoized_fib(80))
