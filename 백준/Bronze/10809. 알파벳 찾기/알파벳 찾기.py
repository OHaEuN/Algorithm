S = input()
alphabet ='abcdefghijklmnopqrstuvwxyz'
answer = []
for c in alphabet:
    if c in S:
        answer.append(S.index(c))
    else:
        answer.append(-1)
    
print(' '.join(map(str,answer)))