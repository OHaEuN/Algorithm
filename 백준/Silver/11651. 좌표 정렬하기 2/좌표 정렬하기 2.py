import sys
inputf= sys.stdin.readline

N = int(inputf())
arr=[]
for _ in range(N):
    arr.append(list(map(int,inputf().split())))
arr = sorted(arr, key = lambda x: (x[1],x[0]))

for a in arr:
    print(*a)