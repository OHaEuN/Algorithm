import sys
import heapq
input = sys.stdin.readline

N = int(input())
q = []

for _ in range(N):
    q.append(int(input()))

heapq.heapify(q)
qsum = 0

while len(q) >=2 :
    num1 = heapq.heappop(q)
    num2 = heapq.heappop(q)
    qsum = qsum + num1 + num2
    if len(q) == 0 :
        break
    else:
        heapq.heappush(q, num1 + num2)

print(qsum)