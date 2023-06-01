N,X = map(int,input().split())
arr = list(map(int,input().split()))
answer =[]
for n in arr:
    if n <X:
        answer.append(n)
print(' '.join(map(str,answer)))