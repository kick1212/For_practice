def solution(n):
    a, b = 1, 0
    for i in range(n+1):
        a, b = b, a + b
        # print(a, b)
    return b % 1000000007