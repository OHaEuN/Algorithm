import sys
inputf= sys.stdin.readline

N,M = map(int,inputf().split())
noL =set()
noS =set()

for _ in range(N):
    noL.add(inputf().strip())
for _ in range(M):
    noS.add(inputf().strip())

answer = sorted(list(noL & noS))
print(len(answer))
for i in answer:
    print(i)