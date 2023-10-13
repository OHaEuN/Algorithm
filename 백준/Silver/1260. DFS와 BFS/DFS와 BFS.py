import sys
inputf= sys.stdin.readline

N,M,V = map(int,inputf().split())

matrix = [[] for _ in range(N+1)]
for _ in range(M):
    a,b =map(int, inputf().split())
    matrix[a].append(b)
    matrix[b].append(a)

def dfs():
    visited=[0 for _ in range(N+1)]
    answer = []

    def visit(n):
        if visited[n] == 0:
            visited[n] = 1
            answer.append(n)
            for i in sorted(matrix[n]):
                visit(i)
    visit(V)
    print(*answer)

                

def bfs():
    visited=[0 for _ in range(N+1)]
    queue = [V]
    answer = []
    while queue:
        v = queue.pop(0)
        if visited[v] == 0:
            visited[v] = 1
            answer.append(v)
            for i in sorted(matrix[v]):
                queue.append(i)
    print(*answer)


dfs()
bfs()