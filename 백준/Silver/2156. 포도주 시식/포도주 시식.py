import sys
input = sys.stdin.readline

n = int(input())
arr =[]
for i in range(n):
    arr.append(int(input()))

if n<3:
    sum = 0
    for i in range(n):
        sum = sum + arr[i]
    print(sum)
elif n == 3:
    sum = max(arr[0]+arr[1],arr[1]+arr[2],arr[0]+arr[2])
    print(sum)
else:
    sum = [0]*n
    sum[0] = arr[0]
    sum[1] = arr[0]+arr[1]
    sum[2] = max(arr[0]+arr[1],arr[1]+arr[2],arr[0]+arr[2])

    for i in range(3,n):
        sum[i]=max(sum[i-2]+arr[i],sum[i-3]+arr[i-1]+arr[i],sum[i-1])
            
    print(max(sum))