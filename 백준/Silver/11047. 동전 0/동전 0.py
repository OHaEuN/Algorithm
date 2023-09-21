import sys
inputf= sys.stdin.readline

N,T = map(int,inputf().split())
value =[] 
for _ in range(N):
    value.append(int(inputf()))

ans = 0
for i in range(N-1,-1,-1):
    if (value[i]<=T):
        ans += T//value[i]
        T -= (T//value[i])*value[i]
print(ans)