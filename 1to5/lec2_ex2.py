# 리스트에서 원소 찾아내기
def solution(L, x):
    answer = []
    for idx, ele in enumerate(L):
        if ele == x:
            answer.append(idx)

    return answer if answer else [-1]