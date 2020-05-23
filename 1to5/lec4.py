# 재귀함수(recursive functions)
# 하나의 함수에서 자신을 다시 호출하여 작업을 수행하는 것
def df_sum(n):
    print(n)
    if n <= 1:
        return n
    else:
        return n + df_sum(n-1)
df_sum(3)

# 재귀함수를 호출할 때는 종결조건이 중요
# 인자의 경우에 따라 종료할 수 있게 작성해야 함.
# 모든 재귀 알고리즘은 반복문으로도 작성 가능(iterative version)
# 단 매번 함수를 호출해야하므로 효율은 떨어짐.