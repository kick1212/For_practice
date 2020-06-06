# 이진 트리의 순회 - 넓이 우선 순회(Breadth First Traversal)
"""
원칙
- 수준이 낮은 노드를 우선 방문
- 같은 수준의 노드들 사이에는, 부모 노드의 방문 순서에 따라 방문
왼쪽 자식 노드를 오른쪽 자식보다 먼저 방문
재귀적 방법은 적합하지 않으며,  큐를 활용한다.
"""


class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r

    def bft(self):
        traversal = []
        q = ArrayQueue()

        if self.root:
            q.enqueue(self.root)

        while not q.isEmpty():
            visited = q.dequeue()
            traversal.append(visited.data)
            if visited.left:
                q.enqueue(visited.left)
            if visited.right:
                q.enqueue(visited.right)

        return traversal


def solution(x):
    return 0

