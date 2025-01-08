def memoized_fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = memoized_fib(n - 1, memo) + memoized_fib(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    print(memoized_fib(10))
