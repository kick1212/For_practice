# 연결 리스트 2
# 연결 리스트 연산 - 원소의 삽입
class Node:

    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

# 원소 삽입 메서드 : insertAt
    def insertAt(self, pos, newNode):
        # pos가 삽입할 수 없는 위치라면 False 리턴
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        # pos가 가리키는 위치에(1<=pos<=nodeCount+1) newNode를 삽입
        # 삽입할 노드가 첫번째에 위치할 경우
        if pos == 1:
            # 이미 존재하는 맨 앞 노드를 새 노드의 다음으로 설정하고, 새 노드를 맨 앞 노드로 설정
            newNode.next = self.head
            self.head = newNode

        else:
            # pos가 마지막에 넣을 위치인 경우 이전 노드는 맨 끝 노드
            if pos == self.nodeCount + 1:
                prev = self.tail
            # pos가 중간에 있는 경우
            else:
                # 이전 노드는 pos-1번째 노드, getAt으로 앞에서부터 탐색해야 함.
                prev = self.getAt(pos - 1)
            # prev.next = pos번째 노드를 새 노드의 다음으로 설정
            newNode.next = prev.next
            # newNode는 새로운 pos번째 노드로 prev의 다음으로 설정
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode
        # 노드의 길이를 1 증가 시킴킴
        self.nodeCount += 1
        # 원소 삽입에 성공했다면 True를 리턴
        return True

    def getLength(self):
        return self.nodeCount

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result
    # 두 리스트의 연결
    def concat(self, L):
        self.tail.next = L.head
        if L.tail:  # L이 비어있을 수 있으므로 조건 체크
            self.tail = L.tail
        self.nodeCount += L.nodeCount

# 연결 리스트 원소 삽입의 복잡도
## 맨 앞 또는 맨 끝에 삽입하는 경우: O(1)
## 중간에 삽입하는 경우: O(N)

# 연결 리스트 원소의 삭제
# pos-1 > pos > pos+1
# pos-1을 prev로 가르킴,
# 링크 조정은 prev.next <- curr.next
# pos를 curr로 설정하고 리턴,
# 마지막으로 노드카운트를 1 감소

# 유의점
# 삭제하려는 node가 맨 앞의 것일 때: prev없음, head 조정 필요
# 리스트 맨 끝의 node를 삭제할 때: tail 조정 필요
# 유일한 노드를 삭제할 때?...??

# 원소의 삭제 시간복잡도
## 맨 앞에 삽입하는 경우: O(1)
## 중간 또는 맨 끝에 삽입하는 경우: O(N)