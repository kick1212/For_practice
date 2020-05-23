# 정렬과 탐색

list1 = [2, 7, 1, 6, 5, 9, 8]
list2 = sorted(list1)
list2
list1
list1.sort()
list1 # 리스트 자체가 변화

# 정렬의 순서를 반대로, 즉 내림차순(큰 값부터 작은값으로)
list2 = sorted(list1, reverse=True)
list1.sort(reverse=True)

# 문자를 정렬하는 경우
# 정렬 순서는 사전순서(알파벳순서)를 따름
# 키를 이용하여 정렬하는 경우 - list
list1 = ['abcd', 'xyz', 'spam']
sorted
# 키를 이용하여 정렬하는 경우 - dic
list1 = [{'name':'john', 'score':83}, {'name':'paul', 'score':92}]
list1.sort(key=lambda x:x['score'], reverse=True) # 레코드들을 점수가 높은 순으로 정렬
list1

# 탐색알고리즘1. 선형탐색(linear search) 또는 순차탐색
# 리스트의 길이에 비례하는 시간이 소요
# 최악의 경우 모든 원소를 다 비교해 봐야함.
def linear_search(L, x):
    i = 0
    while i < len(L) and L[i] != x:
        i += 1
    if i < len(L):
        return i
    else:
        return -1
linear_search([3, 8, 2, 7, 4, 10], 4)
linear_search([3, 8, 2, 7, 4, 10], 6)

# 탐색알고리즘2. 이진탐색
# 탐색하려는 리스트가 이미 정렬되어 있는 경우
# 한번 비교가 일어날때마다 리스트를 반씩 줄임
# 시간복잡도가 O(log n)

# 선형탐색과 이진탐색 비교
# 이진 탐색은 정렬해야하므로 이때도 시간이 소요됨
# 상황에 따라 선호되는 탐색 방법이 다름름