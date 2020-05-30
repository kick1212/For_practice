# 스택(Stacks)
"""
자료를 보관할 수 있는 선형 구조(데이터 아이템이 일렬로 늘어져 있음)
단, 넣을 때에는 한 쪽 끝에서 넣어야 하고 > push 연산
꺼낼 때에는 같은 쪽에서 뽑아 꺼내야 하는 제약이 있다. > pop 연산
즉 후입선출(LIFO, Last In First Out) 특징을 갖는 선형 자료구조

스택의 추상적 자료구조 구현
1) 배열을 이용한 구현
> 파이썬 리스트와 메서드들을 이용
2) 연결 리스트를 이용한 구현
> 지난 강의에서 마련한 양방향 연결 리스트 이용
* 연산 정의
- size() : 현재 스택에 들어있는 원소의 수를 구함
- isEmpty() : 현재 스택이 비어 있는지를 판단
- push(x) : 데이터 원소 x를 스택에 추가
- pop() : 스택의 맨 위에 저장된 데이터 원소를 제거(또는 반환)
- peek() : 스택의 맨 위에 저장된 데이터 원소를 반환(제거하지 않음)
"""
from doublylinkedlist import Node
from doublylinkedlist import DoublyLinkedList

class ArrayStack:

	def __init__(self):
		self.data = []

	def size(self):
		return len(self.data)

	def isEmpty(self):
		return self.size() == 0

	def push(self, item):
		self.data.append(item)

	def pop(self):
		return self.data.pop()

	def peek(self):
		return self.data[-1]

class LinkedListStack:

	def __init__(self):
		self.data = DoublyLinkedList()

	def size(self):
		return self.data.getLength()

	def isEmpty(self):
		return self.size() == 0

	def push(self, item):
		node = Node(item)
		self.data.insertAt(self.size() + 1, node)

	def pop(self):
		return self.data.popAt(self.size())

	def peek(self):
		return self.data.getAt(self.size()).data

