import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

stack = []
ans = []

for i in range(N):
    while stack and arr[stack[-1]]<arr[i]:
        stack.pop()
    if stack:
        ans.append(stack[-1] +1)
    else:
        ans.append(0)
    stack.append(i)

print(' '.join(list(map(str, ans))))