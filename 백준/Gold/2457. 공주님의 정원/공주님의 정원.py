import sys

n=int(sys.stdin.readline())
arr = []
for _ in range(n):
    start_m, start_d, end_m, end_d = map(int, sys.stdin.readline().split())
    if end_m * 100 + end_d < 301 or start_m * 100 + start_d > 1130:
        continue
    arr.append([start_m * 100 + start_d, end_m * 100 + end_d])
arr.sort()

count=0
current=[0,0]
idx = -1

for i in range(len(arr)):
    if arr[i][0] > 301:
        break
    if arr[i][1] >current[1]:
        current = arr[i]
        idx = i
answer = 1

while current[1] <= 1130:
    next = [-1,-1]
    for i in range(idx,n):
        if arr[i][0]> current[1]:
            break
        if current[0]<arr[i][0] <=current[1]<arr[i][1]:
            if arr[i][1]>next[1]:
                next = arr[i]
                idx = i
    if next[0] == -1:
        print(0)
        exit()
    current = next
    answer +=1

print(answer)