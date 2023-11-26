from itertools import product
def solution(word):
    alphabet = ['A', 'E', 'I', 'O', 'U']
    arr = []
    for i in range(1,6):
        for p in product(alphabet, repeat = i):
            arr.append(''.join(p))
    arr.sort()
    return arr.index(word)+1