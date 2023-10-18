import sys
inputf = sys.stdin.readline
n = int(inputf())
paper = []
for _ in range(n):
    paper.append(list(map(int,inputf().split())))
blue_cnt, white_cnt = 0, 0

def check(x,y,n):
    global blue_cnt, white_cnt
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                next_n = n // 2
                check(x, y, next_n)
                check(x, y + next_n, next_n)
                check(x + next_n, y, next_n)
                check(x + next_n, y + next_n, next_n)
                return
    if color == 0:
        white_cnt += 1
    else:
        blue_cnt += 1
    return

check(0,0,n)
print(white_cnt)
print(blue_cnt)