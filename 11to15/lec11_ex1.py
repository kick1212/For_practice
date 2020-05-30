# 스택 - 수식의 괄호 유효성 검사
"""
수식을 왼쪽부터 한 글자씩 읽어서:
여는 괄호를 만나면 스택에 푸시
닫는 괄호를 만나면
> 스택이 비어 있으면 올바르지 않은 수식
> 스택에서 pop, 쌍을 이루는 여는 괄호인지 검사
>> 맞지 않으면 올바르지 않은 수식
끝까지 검사한 후, 스택이 비어 있어야 올바른 수식
"""

def solution(expr):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    S = ArrayStack()
    for c in expr:
        if c in '({[':
            S.push(c)
        elif c in match:
            if S.isEmpty():
                return False
            else:
                t = S.pop()
                if t != match[c]:
                    return False
    return S.isEmpty()