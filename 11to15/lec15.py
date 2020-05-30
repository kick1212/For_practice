# 환형 큐(Circular Queues)
"""
큐의 활용
: 자료를 생성하는 작업과 그 자료를 이용하는 작업이 비동기적으로 일어나는 경우
: 자료를 생성하는/이용하는 작업이 여러 곳에서 일어나는 경우
: 자료를 생성하는 작업과 그 자료를 이용하는 작업이 양쪽 다 여러 곳에서 일어나는 경우
: 자료를 처리해 새로운 자료를 생성하고, 나중에 그 자료를 또 처리해야 하는 작업인 경우

환형 큐
: 정해진 개수의 저장 공간을 빙 돌려가며 이용
데이터를 집어 넣는 부분에서 포인터는 rear,
꺼내는 부분에서 포인터는 front를 이용
: 큐가 가득 차면 > 더 이상 원소를 넣을 수 없음
:front와 rear을 적절히 활용해야 함.
"""
class CircularQueue:

    def __init__(self, n):
        self.maxCount = n
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.maxCount

    def enqueue(self, x):
        if self.isFull():
            raise IndexError('Queue full')
        self.rear = (self.rear + 1) % self.maxCount
        self.data[self.rear] = x
        self.count += 1

    def dequeue(self):
        if self.isEmpty()
            raise IndexError('Queue empty')
        self.front = (self.front + 1) % self.maxCount
        x = self.data[self.front]
        self.count -= 1
        return x

    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        return self.data[(self.front + 1) % self.maxCount]


