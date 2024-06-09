import sys

inputf = sys.stdin.readline

N,M = map(int,inputf().split())
arr = list(map(int,inputf().split()))
arr.extend(list(map(int,inputf().split())))
arr.sort()
print(*arr)