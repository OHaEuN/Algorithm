import sys
inputf= sys.stdin.readline

N = int(inputf())
num = []
for _ in range(N):
    num.append(int(inputf()))
def pibonacci(t):
    arr =[[1,0],[0,1]]
    if t==0:
        print(*arr[0])
    elif t==1:
        print(*arr[1])
    else:
        i = 2
        while i<t+1:
            arr.append([arr[i-2][0]+arr[i-1][0],arr[i-2][1]+arr[i-1][1]])
            i+=1
        print(*arr[-1])

for n in num:
    pibonacci(n)