# 연결리스트가 유용할 때 : 삽입과 삭제가 빈번하게 발생할 때
# dummy node: 기능을 하지 않고 자리만 잡고 있는 노드
class Node:

	def __init__(self, item):
		self.data = item
		self.next = None

class LinkedList:

	def __init__(self):
		self.nodeCount = 0
		self.head = Node(None)   # head에 더미노드를 생성
		self.tail = None
		self.head.next = self.tail

	def __repr__(self):
		if self.nodeCount == 0:
			return 'LinkedList: empty'

		s = ''
		curr = self.head
		while curr.next:
			curr = curr.next
			s += repr(curr.data)
			if curr.next is not None:
				s += ' -> '
		return s

	def getLength(self):
		return self.nodeCount

	def traverse(self):
		result = []
		curr = self.head
		while curr.next:
			curr = curr.next
			result.append(curr.data)
		return result

	def getAt(self, pos):
		if pos < 0 or pos > self.nodeCount:
			return None

		i = 0
		curr = self.head
		while i < pos:
			curr = curr.next
			i += 1

		return curr

	# 연결 리스트 연산- 원소의 삽입
	# prev가 가리키는 노드의 다음에 newNode를 삽입하고 성공/실패에 따라 True/False를 리턴
	def insertAfter(self, prev, newNode):
		newNode.next = prev.next
		if prev.next is None: # tail의 끝에 삽입할 때(next가 없는 경우)
			self.tail = newNode
		prev.next = newNode
		self.nodeCount += 1
		return True

	# 포지션을 지정하고 원소를 삽입하는 메서드
	def insertAt(self, pos, newNode):
		# pos 범위 조건 확인
		if pos < 1 or pos > self.nodeCount + 1:
			return False

		if pos != 1 and pos == self.nodeCount + 1:
			prev = self.tail
		else:
			prev = self.getAt(pos - 1)
		return self.insertAfter(prev, newNode)

	def concat(self, L):
		self.tail.next = L.head.next
		if L.tail:
			self.tail = L.tail
		self.nodeCount += L.nodeCount

# 연결 리스트 원소의 삭제: prev의 다음 노드를 삭제하고 그 node의 값을 리턴
"""
즉, prev -> curr(삭제할 데이터) -> next
prev가 마지막 node일 때(prev.next == None) > 삭제할 node없음, return None
리스트 맨 끝의 node를 삭제할 때(curr.next == None) > tail 조정 필요
"""
# 연습문제: popAfter(), popAt()은 popAfter()를 호출하여 이용

