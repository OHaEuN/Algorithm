from collections import deque
n=int(input())
answer =[]
for _ in range(n):
    cnt = 1
    N,index=map(int,input().split())
    queue = deque(list(map(int,input().split())))
    while queue:
        maxnum = max(queue)
        popnum = queue.popleft()
        if index == 0:
            if popnum<maxnum:
                queue.append(popnum)
                index = len(queue)-1
            else:
                break
        else:
            if popnum<maxnum:
                queue.append(popnum)
                index-=1
            else:
                index-=1
                cnt+=1
    answer.append(cnt)
    
for i in answer:
    print(i)