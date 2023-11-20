from collections import deque
def solution(queue1, queue2):
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    target = (sum_q1+sum_q2)/2
    length = len(queue1)+len(queue2)
    queue1,queue2 = deque(queue1),deque(queue2)
    count = 0
    while sum_q1!=target and sum_q2!=target:
        if count>length*2:
            return -1
        if sum_q1>=sum_q2 and sum_q1>target:
            n = queue1.popleft()
            queue2.append(n)
            sum_q2+=n
            sum_q1-=n
        else:
            n = queue2.popleft()
            queue1.append(n)
            sum_q1+=n
            sum_q2-=n
        count+=1
    return count