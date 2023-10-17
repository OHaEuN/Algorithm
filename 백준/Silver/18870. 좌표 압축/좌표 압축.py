import sys
inputf= sys.stdin.readline
N = int(inputf())
arr = list(map(int,inputf().split()))
sorted_arr = sorted(list(set(arr)))
dic = dict()
for i in range(len(sorted_arr)):
    dic[sorted_arr[i]]=i
for i in range(N):
    arr[i]=dic[arr[i]]
print(*arr)