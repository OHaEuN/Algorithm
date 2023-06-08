import sys
input=sys.stdin.readline
n = int(input())
arr =[]
stack =[]
for _ in range(n):
    order = input().strip()
    if order[:4] == "push":
        stack.append(order[5:])
    elif order == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1) 
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif order == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)