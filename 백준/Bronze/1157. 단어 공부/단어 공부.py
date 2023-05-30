arr = input().upper()
word =list(set(arr))
prev = 0
answer = ""
for x in word:
    cnt = arr.count(x)
    if cnt > prev:
        prev = cnt
        answer = x
    elif cnt == prev:
        answer = "?"

print(answer)