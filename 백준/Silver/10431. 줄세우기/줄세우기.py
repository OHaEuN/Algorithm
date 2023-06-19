import sys
input = sys.stdin.readline

n = int(input())
answer =[]
for _ in range(n):
    count = 0
    student = list(map(int,input().split()))
    student.pop(0)
    line = []
    for s in student:
        line.append(s)
        line.sort()
        count+=len(line)-(line.index(s)+1)
    answer.append(count)


for i in range(len(answer)):
    print(i+1,answer[i])