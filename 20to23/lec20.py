# 이진 탐색 트리(Binary Search Tree)
"""
이진 탐색 트리
: 모든 노드에 대해서, 왼쪽 서브트리에 있는 데이터는 모두 현재 노드의 값보다 작고
오른쪽 서브트리에 있는 데이터는 모두 현재 노드의 값보다 큰
성질을 만족하는 이진트리
단, 중복되는 원소는 없다고 가정한다. 

장점 : 데이터 원소의 추가, 삭제가 용이
단점 : 공간 소요가 큼

각 노드는 (key, value)의 쌍으로 표현한다.
"""


class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


    def insert(self, key, data):
        if key < self.key:
            if self.left:
                return self.left.insert(key, data)
            else:
                self.left = Node(key, data)

        elif key > self.key:
            if self.right:
                return self.right.insert(key, data)
            else:
                self.right = Node(key, data)

        else:
            raise KeyError('...')


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal


class BinSearchTree:

    def __init__(self):
        self.root = None


    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


def solution(x):
    return 0