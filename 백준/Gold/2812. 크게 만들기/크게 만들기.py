import sys
input = sys.stdin.readline

N, K = map(int,input().split())
arr = list(map(int,input().strip()))
stack = []
cnt = 0

for i in range(N):
    while cnt < K and stack:
        if stack[-1] < arr[i]:
            stack.pop()
            cnt+=1
        elif stack[-1] >= arr[i]:
            break
    stack.append(arr[i])

while cnt < K:
    stack.pop()
    cnt +=1

print(int("".join((map(str,stack)))))