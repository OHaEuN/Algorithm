import sys
input = sys.stdin.readline

n,k = map(int,input().split())
dic = dict()
for _ in range(n):
    a,b,c,d = map(int,input().split())
    dic[a] = [b,c,d]
sorteddic = sorted(dic.items(), reverse=True, key = lambda x: (x[1][0],x[1][1],x[1][2]))
rank = dict()
order = 1
for i in range(len(dic)):
    if i == 0 :
        rank[sorteddic[i][0]] = order
    elif i > 0 and sorteddic[i][1] == sorteddic[i-1][1]:
        rank[sorteddic[i][0]] = order
    else:
        order+=1
        rank[sorteddic[i][0]] = order

print(rank[k])