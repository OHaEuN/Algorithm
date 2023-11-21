from collections import deque
def solution(n, k):
    answer = 0
    k_num_deq = deque()
    while n>0:
        k_num_deq.appendleft(str(n%k))
        n = n//k
    k_num = ''.join(k_num_deq)
    nums = k_num.split("0")
    
    def isPrime(n):
        if n == 1:
            return False
        for i in range(2,int(n**(1/2))+1):
            if n%i ==0:
                return False
        return True
    
    for n in nums:
        if n == "":
            continue
        else:
            if isPrime(int(n))==True:
                answer+=1
                
    return answer