num = int(input())

arr =[]

for i in range(0,num):
    a,b=input().split()
    a=int(a)
    b=int(b)
    arr.append([a,b])

arr.sort(key=lambda x:(x[1],x[0]))
end=0
times=0

for a,b in arr:
    if a>=end:
        times+=1
        end=b

print(times)
