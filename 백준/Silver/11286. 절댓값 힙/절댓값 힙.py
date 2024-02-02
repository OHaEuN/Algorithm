import sys
inputf = sys.stdin.readline
from heapq import heappush, heappop

N = int(inputf())
arr = []

def pop():
    if len(arr)==0:
        print(0)
    else:
        abs_n, n = heappop(arr)
        print(n)

for _ in range(N):
    T = int(inputf())
    if T == 0:
        pop()
    else:
        heappush(arr,(abs(T),T))