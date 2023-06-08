import itertools
import sys
input=sys.stdin.readline
n,m = map(int,input().split())
arr =list(map(int,input().split()))
nC3 = list(itertools.combinations(arr,3))
answer = 0
for nums in nC3:
    if sum(nums) <= m:
        if m-answer > m-sum(nums) :
            answer = sum(nums)
print(answer)