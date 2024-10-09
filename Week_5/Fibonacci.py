'''
Fibonacci(0) = 0
Fibonacci(1) = 1
Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2) for n > 1
'''

def Fibonacci(n):
    val = -1
    if n <= 0:
        val = 0
    elif n == 1:
        val = 1
    else:
        val = Fibonacci(n - 1) + Fibonacci(n - 2)
    return val

if __name__ == "__main__":
    print(f"Fibonacci of 100 is {Fibonacci(100)}")