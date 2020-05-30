# 스택의 응용 - 후위 표기 수식 계산

"""
피연산자를 만나면 스택에 넣음
연산자를 만나면 스택에 들어가 있던 피연산자 두개를 꺼내어 연산을 수행하고
스택에 다시 넣는다
이때 덧셈, 곱셈은 위치가 상관없지만
뺄셈, 나눗셈의 경우 두번째로 팝한 피연산자가 연산자 앞에 있어야함을 유의
수식이 끝나면 스택에서 원소를 꺼냄
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

def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens

def infixToPostfix(tokenList):
    prec = {
        '*': 3,        '/': 3,
        '+': 2,       '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for token in tokenList:
        if token == '(':
            opStack.push(token)
        elif token == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        elif type(token) is int:
            postfixList.append(token)
        else:
            while opStack.size() != 0 and prec[token] <= prec[opStack.peek()]:
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):

    valStack = ArrayStack()

    for token in tokenList:
        if type(token) is int:
            valStack.push(token)
        else:
            a = valStack.pop()
            b = valStack.pop()
            if token == '*':
                valStack.push(b*a)
            elif token == '/':
                valStack.push(b/a)
            elif token == '+':
                valStack.push(b+a)
            else:
                valStack.push(b-a)

    return valStack.pop()

def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val