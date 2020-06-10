# 힙(heaps)
"""
힙이란?
: 이진 트리의 한 종류로,
1. 루트 노드가 언제나 최댓값 또는 최솟값을 가지며
2. 완전 이진 트리여야 한다.
"""

class MaxHeap:

    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)
        idx = len(self.data) - 1

        while idx > 1:
            if self.data[idx] > self.data[idx // 2]:
                self.data[idx], self.data[idx // 2] = self.data[idx // 2], self.data[idx]
                idx = idx // 2
            else:
                break

def solution(x):
    return 0