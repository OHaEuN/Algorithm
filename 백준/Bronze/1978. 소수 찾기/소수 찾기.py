import math

n= int(input())
arr = list(map(int,input().split()))
m=max(arr)
prime =[True for _ in range(m+1)]
prime[1] = False
for i in range(2,int(math.sqrt(m))+1):
    j=2
    if prime[i] == True:
        while i*j <=m:
            prime[i*j] = False
            j+=1
cnt=0
for x in arr:
    if prime[x] == True:
        cnt+=1
print(cnt)