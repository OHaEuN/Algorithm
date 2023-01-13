import sys
num = int(sys.stdin.readline())
arr =[]
for i in range(0,num):
    arr.append(int(sys.stdin.readline()))
arr.sort()

answer=0
for n in range(0,num):
    answer+=abs(arr[n]-(n+1))

print(answer)