import sys
input=sys.stdin.readline
n = int(input())
arr =[]
queue =[]
for _ in range(n):
    order = input().strip()
    if order[:4] == "push":
        queue.append(order[5:])
    elif order == "pop":
        if queue:
            print(queue.pop(0))
        else:
            print(-1) 
    elif order == "size":
        print(len(queue))
    elif order == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif order == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif order == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)