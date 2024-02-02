import sys
inputf = sys.stdin.readline

T = int(inputf())
for _ in range(T):
    answer = 9999999
    N = int(inputf())    
    arr = list(map(str,inputf().split()))
    if N >32:
        print(0)
        continue
    else:
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if i==j or j==k or k==i:
                        continue
                    else:
                        temp = 0
                        for n in range(4):
                            if arr[i][n] != arr[j][n] : temp+=1
                            if arr[j][n] != arr[k][n] : temp+=1
                            if arr[k][n] != arr[i][n] : temp+=1
                        answer = min(answer,temp)
    print(answer)