import sys
inputf= sys.stdin.readline

N = int(inputf())
i = 1
count = 1
while N > i:    
    i += count*6
    count += 1
print(count)