# 연결 리스트(linked lists)

# 추상적 자료구조란?

# 특정원소 참조
def getAt(self, pos):
    if pos <= 0 or pos > self.nodeCount:
        return None
    i = 1
    curr = self.head
    while i < pos:
        curr = curr.next
        i += 1
    return curr

# 배열과 비교한 연결리스트
# 저장공간 : 연속한 위치 / 임의의 위치
# 특정원소지칭 : 인덱스만 지정하면 되어 간편, O(1) / 선형탐색과 유사, O(n)
