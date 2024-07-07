import sys
from collections import Counter

inputf = sys.stdin.readline

N = int(inputf())
arr = []
for _ in range(N):
    arr.append(int(inputf()))

cnt_num = dict(Counter(arr))
sorted_dict = sorted(cnt_num.items(),key = lambda x : (-x[1],x[0]))

print(sorted_dict[0][0])