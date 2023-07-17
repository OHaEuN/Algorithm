import sys
inputf= sys.stdin.readline

N = int(inputf())

answer = 0
if N <60:
    for x in range(N,0,-1):
      if N == x + sum(list(map(int,str(x)))):
         answer = x
else:
    for x in range(N,N-60,-1):
        if N == x + sum(list(map(int,str(x)))):
            answer = x

print(answer)