# 큐(Queues)
"""
자료를 보관할 수 있는 선형구조이다.(스택과 동일)
단, 넣을 때엥는 한 쪽 끝에서 밀어 넣어야 하고 > 인큐 연산
꺼낼 때에는 반대 쪽에서 뽑아 꺼내야 하는 제약이 있음 > 디큐 연산
즉, 선입선출(FIFO, First In First Out) 특징을 갖는 선형 자료구조이다.

큐의 추상적 자료구조 구현
1) 배열을 이용 > 파이썬 빌트인 리스트와 메서드들을 이용
2) 연결 리스트를 이용 > 양방향 연결 리스트 이용
"""
# 이중 연결 리스트로 큐 구현
class LinkedListQueue:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.data.getLength() == 0

    def enqueue(self, item):
        node = Node(item)
        self.data.insertAt(self.data.nodeCount+1, node)

    def dequeue(self):
        return self.data.popAt(1)

    def peek(self):
        return self.data.getAt(1).data
