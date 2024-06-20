import sys
from itertools import combinations
inputf = sys.stdin.readline

N,S = map(int,inputf().split())
arr = list(map(int,inputf().split()))
ans = 0 
for i in range(1,len(arr)+1):
    combi = list(combinations(arr,i))
    for c in combi:
        if sum(c) == S:
            ans+=1
print(ans)