import sys

inputf = sys.stdin.readline
arr = [0,1,2,4] # arr[4] = 7 / arr[5] = 13 << 규칙 보임
for i in range(4,11):
    arr.append(arr[i-1]+arr[i-2]+arr[i-3])

T = int(inputf())
for _ in range(T):
    n = int(inputf())
    print(arr[n])