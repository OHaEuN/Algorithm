import sys
n,k = sys.stdin.readline().split()
n= int(n)
k=int(k)
arr =list(map(int, sys.stdin.readline().split()))
dis =[]

for i in range(n-1):
    dis.append(arr[i+1]-arr[i])
dis.sort()

sum=0
for i in range(0,n-k):
    sum += dis[i]

print(sum)