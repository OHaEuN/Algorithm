def solution(n, computers):
    visited = [[0] * n for _ in range(n)]
    graph = [[] for _ in range(n)]
    count = 0

    def bfs(start):
        queue = [start]
        while queue:
            node = queue.pop(0)
            if visited[node][node] == 0:
                visited[node][node] = 1
                for neighbor in graph[node]:
                    if visited[neighbor][neighbor] == 0:
                        queue.append(neighbor)

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].append(j)

    for i in range(n):
        if visited[i][i] == 0:
            bfs(i)
            count += 1

    return count
