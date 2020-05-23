# 재귀 알고리즘 - 응용
# ex1. 조합의 수 계산하기
def combi(n, m):
    if n == m:
        return 1
    elif m == 0:
        return 1
    else:
        return combi(n-1, m) + combi(n-1, m-1)

# 효율이 떨어져도 경우에 따라 쓸모있을 때가 많다.
