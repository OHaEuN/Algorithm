import sys
input= sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))
A.sort()
m = int(input())
arr = list(map(int,input().split()))
start = 0
end = n-1
def binarySearch(s,e,i):
    start =s
    end =e
    while start<end:
        mid = (start+end)//2
        if A[mid] < i:
            start = mid + 1
        elif A[mid] > i:
            end = mid -1
        else:
            return 1
    if A[end] == i:
        return 1
    else:
        return 0

for i in arr:
    print(binarySearch(start,end,i))