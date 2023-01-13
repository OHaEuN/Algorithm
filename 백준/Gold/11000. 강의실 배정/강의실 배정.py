import heapq
import sys

num = int(sys.stdin.readline())

arr =[]
for i in range(0,num):
    a,b=sys.stdin.readline().split()
    a=int(a)
    b=int(b)
    arr.append([a,b])
arr.sort()

q=[]
heapq.heappush(q,arr[0][1])

for i in range(1,num):
    if arr[i][0]<q[0]:
        heapq.heappush(q,arr[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q,arr[i][1])

print(len(q))