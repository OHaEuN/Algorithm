import sys
inputf= sys.stdin.readline
M,N = map(int,inputf().split())
dic = dict()
question =[]
answer =[]
for i in range(1,M+1):
    dic[inputf().strip()] = str(i)
reverse_dic = {v:k for k,v in dic.items()}

def find(q):
    if q in dic.keys():
        answer.append(dic[q])
    else:
        answer.append(reverse_dic[q])

for _ in range(N):
    find(str(inputf().strip()))

for a in answer:
    print(a)