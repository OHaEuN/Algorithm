from math import factorial

n = int(input())
num = str(factorial(n))
ans = 0
for i in range(len(num)-1,-1,-1):
    if num[i] == '0':
        ans +=1
    else:
        break
print(ans)