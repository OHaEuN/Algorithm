import sys
input=sys.stdin.readline
while 1:
    arr = list(map(int,input().split()))
    if sum(arr) == 0:
        break
    maxN = max(arr)
    arr.remove(maxN)
    if maxN**2 == arr[0]**2 + arr[1]**2:
        print("right")
    else:
        print("wrong")