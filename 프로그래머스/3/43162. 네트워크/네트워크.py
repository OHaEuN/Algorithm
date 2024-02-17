def solution(n, computers):
    visited = [0 for _ in range(n)]
    cnt = 0
    
    def bfs(N):
        nonlocal cnt
        cnt += 1
        queue = [N]
        while queue:
            x = queue.pop(0)
            for i,X in enumerate(computers[x]):
                if X == 1 and not visited[i]:
                    visited[i] = 1
                    queue.append(i)
    
    for N in range(n):
        if not visited[N]:
            bfs(N)
                
    return cnt