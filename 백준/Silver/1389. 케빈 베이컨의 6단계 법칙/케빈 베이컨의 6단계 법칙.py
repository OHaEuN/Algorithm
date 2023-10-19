import sys
inputf = sys.stdin.readline
N,M = map(int,inputf().split()) 
connect = [[] for _ in range(N+1)]
answer = [0 for _ in range(N)]
for _ in range(M):
    a,b = map(int,inputf().split())
    connect[a].append(b)
    connect[b].append(a)
    
def count(x):
    global answer
    kevin = [0]*(N+1)
    visited=[0 for _ in range(N+1)]
    queue = []
    queue.append(x)
    visited[x] = 1
    while len(queue)>0:
        n = queue.pop(0)
        for i in connect[n]:
            if visited[i]==0:
                queue.append(i)
                visited[i]=1
                kevin[i]=kevin[n]+1
    answer[x-1]=sum(kevin)
        
for i in range(1,N+1):
    count(i)
print(answer.index(min(answer))+1)