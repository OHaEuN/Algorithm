import sys

inputf = sys.stdin.readline

E,S,M = map(int,inputf().split())
e,s,m = 15,28,19
i = 1
while 1:
    if (i-E)%e == 0 and (i-S)%s == 0 and (i-M)%m == 0:
        print(i)
        break
    i+=1