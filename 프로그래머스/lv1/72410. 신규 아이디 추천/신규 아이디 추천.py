def solution(new_id):
    #1단계
    new_id = new_id.lower()
    #2단계
    new_id =list(new_id)
    stack=[]
    for w in new_id:
        if w == '-' or w == '_' or w =='.':
            continue
        if w.isalnum() == False:
            stack.append(w)
    for w in stack:
        new_id.remove(w)
    #3단계
    stack=[]
    for w in new_id:
        if stack and stack[-1] == '.' and w =='.':
            continue
        stack.append(w)
    new_id=stack      
    #4단계
    while new_id and new_id[0]=='.':
        new_id.remove('.')    
    print(new_id)
    if new_id :
        while new_id[-1] == '.':
            new_id.pop()
    #5단계
    if len(new_id)==0:
        new_id.append('a')
    #6단계
    if len(new_id)>15:
        while len(new_id)>15:
            new_id.pop()
        if new_id[-1]=='.':
            new_id.pop()
    #7단계
    if len(new_id)<=2:
        while len(new_id)!=3:
            new_id.append(new_id[-1])
    
    return ''.join(new_id)