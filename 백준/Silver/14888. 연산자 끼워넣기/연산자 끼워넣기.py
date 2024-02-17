import sys
from itertools import permutations
inputf = sys.stdin.readline

N = int(inputf())
nums = list(map(int,inputf().split()))
op_num = list(map(int,inputf().split()))
op= ["+","-","*","/"]
ops = []
for i in range(4):
    for _ in range(op_num[i]):
        ops.append(op[i])
Min = 10**9
Max = -1*(10**9)
cals = set(permutations(ops,N-1))

def calculate(o,x,y):
    if o == "+":
        return x+y
    elif o == "-":
        return x-y
    elif o == "*":
        return x*y
    elif o == "/":
        if x < 0:
            return -1*(abs(x)//y)
        else:
            return x//y

for c in cals:
    result = nums[0]
    for i in range(1,N):
        result = calculate(c[i-1],result,nums[i])
    Min = min(Min,result)
    Max = max(Max,result)

print(Max)
print(Min)