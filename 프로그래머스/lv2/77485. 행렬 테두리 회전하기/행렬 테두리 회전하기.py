def solution(rows, columns, queries):
    mtrx = [[j*columns + i + 1 for i in range(columns)] for j in range(rows)]
    answer = []
    for sy,sx,ey,ex in queries:
        changes=[]
        sx -= 1
        sy -= 1
        ex -= 1
        ey -= 1
        # 왼->오
        for x in range(sx, ex):
            changes.append([mtrx[sy][x], x + 1, sy])
        # 위->아래
        for y in range(sy, ey):
            changes.append([mtrx[y][ex], ex, y + 1])
        # 오->왼
        for x in range(ex, sx, -1):
            changes.append([mtrx[ey][x], x - 1, ey])
        # 아래->위
        for y in range(ey, sy, -1):
            changes.append([mtrx[y][sx], sx, y - 1])
        changes.sort()
        for n,x,y in changes:
            mtrx[y][x] = n
        answer.append(changes[0][0])
        
    return answer