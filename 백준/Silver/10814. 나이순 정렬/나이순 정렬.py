import sys
input=sys.stdin.readline
n = int(input())
dic =dict()
for _ in range(n):
    age, name = map(str,input().split())
    age =int(age)
    if age in dic:
        dic[age].append(name)
    else:
        dic[age] = [name]
sortedKey = sorted(dic)
for i in sortedKey:
    for value in dic[i]:
        print(i,value)