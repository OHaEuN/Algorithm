import sys
inputf= sys.stdin.readline

S = inputf().strip()
count_0 = 0
count_1 = 0
k = 0
for i in S:
    if i != k:
        if i == "0":
            count_0 += 1
            k = "0"
        elif i == "1":
            count_1 += 1
            k = "1"

print(min(count_1,count_0))