import sys
inputf = sys.stdin.readline
Line = inputf().strip()
arr = []
queue = []
for l in Line:
    if l == "-" or l == "+":
        arr.append(int("".join(queue)))
        queue = []
        arr.append(l)
    else:
        queue.append(l)
if len(queue)>0:
    arr.append(int("".join(queue)))
    queue = []
is_minus = False
answer = []
for i in range(len(arr)):
    if arr[i] == "-":
        if is_minus:
            answer.append(sum(queue)*-1)
            queue =[]
        else:
            is_minus=True
    elif arr[i] == "+":
        continue
    else:
        if is_minus:
            queue.append(arr[i])
        else:
            answer.append(arr[i])

if len(queue)>0:
    answer.append(sum(queue)*-1)
print(sum(answer))