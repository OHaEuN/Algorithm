import sys
sys.setrecursionlimit(10000)
input_func = sys.stdin.readline
T = int(input_func())
dx=[1,-1,0,0]
dy=[0,0,1,-1]
answer =[]
for _ in range(T):
    M,N,K = map(int,input_func().split())
    mtrx = [[0 for _ in range(M)] for _ in range(N)]

    def bfs(x,y):
        if mtrx[y][x] == 1:
            mtrx[y][x] = 0
            for i in range(4):
                mx = x+dx[i]
                my = y+dy[i]
                if 0<=mx<M and 0<=my<N:
                    bfs(mx,my)

    for __ in range(K):
        X,Y = map(int,input_func().split())
        mtrx[Y][X] = 1
    
    count = 0
    for y in range(N):
        for x in range(M):
            if mtrx[y][x] == 1:
                count+=1
                bfs(x,y)
    answer.append(count)

for n in answer:
    print(n)