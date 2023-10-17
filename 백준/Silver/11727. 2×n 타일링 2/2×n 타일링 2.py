import sys
inputf= sys.stdin.readline
N = int(inputf())
answer = [1,3]
for i in range(2,N):
    answer.append((answer[i-2]*2+answer[i-1])%10007)
print(answer[N-1])