from itertools import combinations
from math import sqrt
def is_prime_num(n):
        for i in range(2,int(sqrt(n))+1):
            if n%i == 0:
                return False
        return True

def solution(nums):
    answer = 0
    com = list(combinations(nums,3))
    for c in com:
        if is_prime_num(sum(c)):
            answer +=1
    return answer