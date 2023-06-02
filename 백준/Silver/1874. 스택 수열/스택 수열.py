n = int(input())
target = []
for _ in range(n):
    target.append(int(input()))

arr = sorted(target)
stack=[]
sequence =[]
answer =[]

def popTarget(t):
    while arr or stack:
        if stack and stack[-1]==t:
            answer.append("-")
            sequence.append(stack.pop())
            break
        elif arr:
            pushNum = arr.pop(0)
            stack.append(pushNum)
            answer.append("+")
        else:
            break

for i in target:
    popTarget(i)

if sequence == target:
    for i in answer:
        print(i)
else:
    print("NO")