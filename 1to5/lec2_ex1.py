# 리스트에 새로운 요소 삽입하기
def solution(L, x):
    for idx, ele in enumerate(L):
        if ele > x:
            L.insert(idx, x)
            return L
    L.append(x)
    return L