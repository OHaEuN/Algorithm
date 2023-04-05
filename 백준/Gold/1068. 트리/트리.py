import sys

input = sys.stdin.readline

N = int(input())
arr= list(map(int,input().split()))
D = int(input())
setArr = set(arr)


def DeleteLeaf(D, arr):
    arr[D] = -2
    if D in setArr:
        for i in range(len(arr)):
            if arr[i] == D:
                DeleteLeaf(i, arr)

DeleteLeaf(D, arr)
count = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        count += 1

print(count)