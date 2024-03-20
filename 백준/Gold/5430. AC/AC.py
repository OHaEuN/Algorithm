import sys
inputf = sys.stdin.readline
from collections import deque

T = int(inputf())

for _ in range(T):
    p = inputf().strip()
    n = int(inputf())
    arr = inputf().strip()[1:-1].split(',')
    
    if n == 0:
        arr = []

    d = True
    error = False

    for cmd in p:
        if cmd == 'R':
            d = not d
        elif cmd == 'D':
            if not arr:
                error = True
                break
            if d:
                arr.pop(0)
            else:
                arr.pop()

    if error:
        print("error")
    else:
        if d:
            print('[' + ','.join(arr) + ']')
        else:
            print('[' + ','.join(reversed(arr)) + ']')
