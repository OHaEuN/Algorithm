import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n):
    arr = list(map(int,input().split()))
    num = arr[0]
    index= 1
    while arr[index] != -1 :
        graph[num].append(arr[index:index+2])
        index +=2

def dfs(x, wei):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei + b)

distance = [-1]*(n+1)
distance[1] = 0
dfs(1,0)

start = distance.index(max(distance))
distance = [-1]*(n+1)
distance[start] = 0
dfs(start,0)

print(max(distance))