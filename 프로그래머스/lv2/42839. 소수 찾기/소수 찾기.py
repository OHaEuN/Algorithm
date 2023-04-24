from itertools import permutations
def solution(numbers):

    def primenumber(x):
        for i in range(2, x):
    	    if x % i == 0:
        	    return False
        return True
    
    arr=[]
    all =[]
    answer=0
    
    for i in range(1, len(numbers)+1):
        arr.extend(permutations(numbers,i))
    
    for n in arr:
        all.append(int(''.join(n)))
    all = set(all)

    for x in all:
        if x != 0 and x!=1:
            if primenumber(x) == True :
                answer +=1
            
    return answer