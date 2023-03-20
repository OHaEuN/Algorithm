import sys
input = sys.stdin.readline

N, W, L = map(int,input().split())
arr = list(map(int,input().split()))
q = []
cnt = 0

while arr : # 마지막 트럭이 다리에 올라오면 끝남
    truck = arr[0]
              
    if len(q) < W :
         if sum(q) + truck <= L:
              q.append(truck)
              arr.pop(0)
              cnt +=1
         else :
              q.append(0)
              cnt +=1
    
    if len(q) == W :
        if sum(q) > 0:
            q.pop(0)
            
print(cnt + W)