# 양방향 연결 리스트(doubly linked lists)
# 다음 노드로도 이전 노드로도 진행 가능
# 리스트 처음과 끝에 dummy node를 둠 > 데이터를 담고 있는 노드들이 모두 같은 모양이어서
# 코드 작성이 쉬워짐

class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr.next.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next.next is not None:
                s += ' -> '
        return s


    def getLength(self):
        return self.nodeCount

    # 리스트 순회
    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result


    # 특정 원소 얻어내기
    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None
        # 절반 이후에 있다면 역방향으로 가도록 함
        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr

    # 원소 삽입
    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

# 연습문제 - 양방향 연결 리스트 메서드 구현
# 연습문제 - 노드가 주어졌을 때 다음, 이전의 노드를 추출, 특정 번째의 노드 추출
# 연습문제 - 리스트 연결하기