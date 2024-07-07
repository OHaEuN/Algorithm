import sys
inputf = sys.stdin.readline

N = int(inputf())
arr = []
for _ in range(N):
    arr.append(list(map(str,inputf().split())))

arr.sort(key=lambda x : (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in arr:
    print(i[0])