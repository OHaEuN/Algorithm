import sys
s = sys.stdin.readline()

stack=[]
answer=[]
bracket=False
for w in s:
    if w == '<':
        bracket = True
    elif w == '>':
        answer.append(w)
        bracket = False
        continue
    elif w == ' ':
        for i in range(0, len(stack)):
            answer.append(stack.pop())
        answer.append(w)
        continue
        
    if bracket == False:
        stack.append(w)
    elif bracket == True:
        for i in range(0, len(stack)):
            answer.append(stack.pop())
        answer.append(w)

stack.pop()
for i in range(0, len(stack)):
    answer.append(stack.pop())

print(''.join(answer))