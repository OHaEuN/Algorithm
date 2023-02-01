import sys
n = int(sys.stdin.readline())
arr =list(map(int, sys.stdin.readline().split()))

arr.sort()
avg = (arr[n-1]-arr[0])//2
median = (n-1)//2

# for i in range(median-1,0,-1):
#     if abs(arr[i]-avg)<=abs(arr[median]-avg):
#         median = i
#     else:
#         break

# for i in range(median+1,n):
#     if abs(arr[i]-avg)<abs(arr[median]-avg):
#         median = i
#     else:
#         break

print(arr[median])