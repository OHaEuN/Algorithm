import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())

def cntChange(i, j):
    Wcnt = 0
    Bcnt = 0
    for a in range(i, i+8):
        for b in range(j, j+8):
            color = board[a][b]
            if (a+b)%2==0:
                if color != "W":
                    Wcnt+=1
                elif color != "B":
                    Bcnt+=1
            else:
                if color != "W":
                    Bcnt+=1
                elif color != "B":
                    Wcnt+=1
    return min(Wcnt,Bcnt)

answer = 100
for i in range(0, n-7):
    for j in range(0, m-7):
        answer = min(answer, cntChange(i, j))

print(answer)