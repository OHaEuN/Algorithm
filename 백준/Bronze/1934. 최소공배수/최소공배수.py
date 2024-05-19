import sys
from math import lcm

inputf = sys.stdin.readline

T = int(inputf())
for _ in range(T):
    ans = 1
    a,b = map(int,inputf().split())
    print(lcm(a,b))