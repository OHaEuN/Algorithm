import sys
inputf= sys.stdin.readline

N=int(inputf())
arr = list(map(int,inputf().split()))
arr.sort()
ans =0 
for i in range(N):
    ans += arr[i]*(N-i)
print(ans)