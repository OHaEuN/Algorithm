import sys
n,m = sys.stdin.readline().split()
n= int(n)
m=int(m)
arr = []
count=dict()

for i in range(n):
    word=sys.stdin.readline().strip()
    if len(word)>=m:
        if count.get(word):
            count[word][0] +=1
        else:
            count[word] =[1,len(word),word]

arr = sorted(count.items(), key= lambda x: (-x[1][0], -x[1][1], x[1][2]))


for i in range(len(arr)):
    print(arr[i][0])