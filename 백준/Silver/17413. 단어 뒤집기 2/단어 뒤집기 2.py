import sys
inputf =sys.stdin.readline
S = inputf().strip()
stack = []
answer = []
is_in = False
for s in S:
    if s == "<":
        if stack:
            for _ in range(len(stack)):
                answer.append(stack.pop())
        is_in = True
    elif s == ">":
        is_in = False
        answer.append(s)
        continue
    elif is_in == False and s == " ":
        if stack:
            for _ in range(len(stack)):
                answer.append(stack.pop())
        answer.append(" ")
        continue
    
    if is_in:
        answer.append(s)
    else:
        stack.append(s)

if stack:
    for _ in range(len(stack)):
        answer.append(stack.pop())

print(''.join(answer))