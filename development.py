from collections import deque
from math import ceil

def solution(progresses, speeds):
    new_list = deque()

    for i in range(len(progresses)):
        new_list.append(ceil((100 - progresses[i]) / speeds[i]))

    cnt = 1
    max_value = new_list[0]
    result = []

    for i in range(1, len(new_list)):
        if max_value >= new_list[i]:
            cnt += 1
        else:
            result.append(cnt)
            cnt = 1
            max_value = new_list[i]
    result.append(cnt)

    return result