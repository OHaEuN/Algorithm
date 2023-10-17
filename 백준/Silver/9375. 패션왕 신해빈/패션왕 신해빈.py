import sys
inputf= sys.stdin.readline
N = int(inputf())
for _ in range(N):
    n = int(inputf())
    dic=dict()
    for _ in range(n):
        name, category = map(str,inputf().split())
        if category in dic.keys():
            dic[category].append(name)
        else:
            dic[category] = [name]
    answer = 1
    for k in dic.keys():
        answer = answer*(len(dic[k])+1)
    print(answer-1)