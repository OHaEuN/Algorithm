import sys

inputf = sys.stdin.readline

N = int(inputf())
cards = list(map(int,inputf().split()))
M = int(inputf())
arr = list(map(int,inputf().split()))
cards.sort()

def bisect(n):
    s,e=0,N-1
    while s<e:
        mid = (s+e)//2
        if cards[mid]>n:
            e = mid-1
        elif cards[mid]<n:
            s = mid+1
        else:
            s=mid
            e=mid-1
    return cards[s]

ans=[]
for i in arr:
    if i ==bisect(i):
        ans.append(1)
    else:
        ans.append(0)
print(*ans)