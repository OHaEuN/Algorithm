n,k = map(int,input().split())
dic = dict()
for _ in range(n):
    a,b,c,d = map(int,input().split())
    dic[a] = [b,c,d]
sorteddic = sorted(dic.items(), reverse=True, key = lambda x: (x[1][0],x[1][1],x[1][2]))
rank = dict()
for i in range(len(sorteddic)):
    rank[sorteddic[i][0]] = sorteddic[i][1]

for i in range(0,k):
    if rank[k] == rank[i+1]:
        print(i+1)
        break