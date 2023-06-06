import sys
input = sys.stdin.readline

n = int(input())
arr =[]
for _ in range(n):
    arr.append(int(input()))
arr.sort()

def countMost():
    dic = dict()
    for i in arr:
        if i in dic:
            dic[i] +=1
        else:
            dic[i] = 1
    mx = max(dic.values())
    mx_dic =[]
    for i in dic:
        if mx ==dic[i]:
            mx_dic.append(i)
    if len(mx_dic)>1:
        print(mx_dic[1])
    else:
        print(mx_dic[0])

print(round(sum(arr)/n))
print(arr[n//2])
countMost()
print(abs(max(arr)-min(arr)))