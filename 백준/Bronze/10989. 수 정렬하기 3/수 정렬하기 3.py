import sys
inputf= sys.stdin.readline

N = int(inputf())
num_list = [0] * 10001

for _ in range(N):
    num_list[int(inputf())] +=1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)