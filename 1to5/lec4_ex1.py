# Fibonacci sequence
# 1. recursive version
def fib_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

# 2. iterative version
def fib_ite(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a