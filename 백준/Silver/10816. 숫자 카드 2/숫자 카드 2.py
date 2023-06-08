import sys
input=sys.stdin.readline
n = int(input())
card = list(map(int,input().split()))
m = int(input())
findNum = list(map(int,input().split()))
answer = []
counter = {}
for i in card:
    counter[i] = counter.get(i,0)+1
for i in findNum:
    answer.append(counter.get(i,0))
print(*answer)