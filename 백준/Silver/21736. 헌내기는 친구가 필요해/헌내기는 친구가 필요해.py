import sys
inputf = sys.stdin.readline
sys.setrecursionlimit(10**7)
N,M = map(int,inputf().split())
campus = []
visited=[[0]*(M) for _ in range(N)]
# I 위치 파악
ix,iy = 0,0
for i in range(N):
    row=inputf().strip()
    if "I" in row:
        iy = i
    campus.append(row)
ix = campus[iy].index("I")

dx = [0,0,1,-1]
dy = [1,-1,0,0]
count = 0
def findP(x,y):
    global visited
    global count
    visited[y][x] = 1
    for i in range(4):
        mx = x+dx[i]
        my = y+dy[i]
        if 0<=mx<M and 0<=my<N:
            if visited[my][mx] == 0 and campus[my][mx] !="X":
                if campus[my][mx] == "P":
                    count+=1
                findP(mx,my)
findP(ix,iy)
if count>0:
    print(count)
else: 
    print("TT")