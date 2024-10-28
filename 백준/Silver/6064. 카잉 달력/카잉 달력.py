import sys
inputf = sys.stdin.readline

k = int(inputf())

def calculate(m, n, x, y):
    k = x 
    while k <= m * n: 
        if (k - x) % m == 0 and (k - y) % n == 0: 
            return k
        k += m 
    return -1


for _ in range(k):
    m, n, x, y = map(int, sys.stdin.readline().split())

    print(calculate(m, n, x, y))