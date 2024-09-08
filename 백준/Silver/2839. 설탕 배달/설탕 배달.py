N = int(input())
bag=0

while(N>0):
    if (N%5==0):
        bag+=N//5
        N=N%5
    else:
        bag+=1
        N-=3

if N==0:
    print(bag)
else:
    print(-1)