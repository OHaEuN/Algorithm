import sys

inputf = sys.stdin.readline

n = int(inputf())
ans = [0,0,0]
papers = []

for _ in range(n):
    row = list(map(int, inputf().split()))
    papers.append(row)

def check(row, col, n):
    global ans
    curr = papers[row][col]

    for i in range(row, row + n):
        for j in range(col, col + n):
            if papers[i][j] != curr:
                next_n = n // 3
                check(row, col, next_n)  
                check(row, col + next_n, next_n)  
                check(row, col + (2 * next_n), next_n)  
                check(row + next_n, col, next_n)  
                check(row + next_n, col + next_n, next_n)  
                check(row + next_n, col + (2 * next_n), next_n) 
                check(row + (2 * next_n), col, next_n)  
                check(row + (2 * next_n), col + next_n, next_n) 
                check(row + (2 * next_n), col + (2 * next_n), next_n) 
                return

    if curr == -1:
        ans[-1]+=1
    elif curr == 0:
        ans[0]+=1
    elif curr == 1:
        ans[1]+=1
    return

check(0, 0, n)

print(ans[-1])
print(ans[0])
print(ans[1])