# 이진탐색 구현
def solution(L, x):
    idx = -1
    lower, upper = 0, len(L) - 1
    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x:
            return middle
        elif L[middle] <= x:
            lower = middle + 1
        else:
            upper = middle - 1
    return idx