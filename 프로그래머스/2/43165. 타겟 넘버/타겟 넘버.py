from collections import deque

def solution(numbers, target):
    q = deque([0])
    for num in numbers:
        prevQueueCnt = len(q)
        for _ in range(prevQueueCnt):
            prev = q.popleft()
            q.append(prev+num)
            q.append(prev-num)
    
    return q.count(target)