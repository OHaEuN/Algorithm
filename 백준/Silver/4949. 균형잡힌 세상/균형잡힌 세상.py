import sys
inputf= sys.stdin.readline
answer =[]
while 1:
    Sarr = inputf().rstrip()
    stack =[]
    if Sarr == '.':
        break

    for i in Sarr:
        if i =="(":
            stack.append("(")
        elif i =="[":
            stack.append("[")
        elif i ==")":
            if len(stack)!=0 and stack[-1] == "(":
                    stack.pop()
            else:
                stack.append(")")
                break
        elif i =="]":
            if len(stack)!=0 and stack[-1] == "[":
                    stack.pop()
            else:
                stack.append("]")
                break
    if len(stack) > 0:
        print("no")
    else: 
        print("yes")