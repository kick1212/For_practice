# 스택의 응용 - 수식의 후위 표기법
"""
중위 표현식을 후위 표현식으로 바꾸기
ex1) a * b + c -> ab*c+
ex2) a + b * c -> abc*+
우선순위가 동일하면 스택에서 꺼내기
우선순위가 나중 것이 먼저이면 갖다가 쓰기
우선순위가 나중 것이 나중이면 스택에서 꺼내고 나중 것을 스택에 넣기

즉, 중위 표현식을 왼쪽부터 한 글자씩 읽어서
> 피연산자이면 그냥 출력
> '('이면 스택에 푸시
> 닫는 괄호이면 여는 괄호가 나올때까지 스택에서 팝, 출력
> 연산자이면 스택에서 이보다 높(거나 같)은 우선 순위 것들을 팝, 출력
그리고 이 연산자는 스택에 푸시
스택에 남아있는 연산자는 모두 팝, 출력

코드 구현 힌트
스택의 맨 위에 있는 연산자와의 우선순위 비교> peek() 연산 이용
스택에 남아 있는 연산자 모두 팝하는 순환문> whille not opStack.isEmpty():
"""

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

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    for s in S:
        if s == '(':
            opStack.push(s)
        elif s == ')':
            while opStack.peek() != '(':
                answer += opStack.pop()
            opStack.pop()
        elif s.isalpha():
            answer += s
        else:
            while opStack.size() != 0 and prec[s] <= prec[opStack.peek()]:
                answer += opStack.pop()
            opStack.push(s)

    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer