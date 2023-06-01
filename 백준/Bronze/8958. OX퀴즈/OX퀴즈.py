n = int(input())
arr=[]
answer =[]
for _ in range(n):
    arr.append(input())

for ox in arr:
    score = 0
    p = 0
    for c in ox:
        if c == "O":
            p +=1
            score += p
        else:
            p = 0
    answer.append(score)

for a in answer:
    print(a)