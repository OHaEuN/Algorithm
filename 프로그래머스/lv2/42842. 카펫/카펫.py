def solution(brown, yellow):
    answer =[]
    
    if yellow == 1: 
        return [3,3]
    
    for i in range(1,yellow):
        if yellow % i == 0 and brown == 4 + 2*i + 2*(yellow/i):
            answer = [yellow/i+2,i+2]
            
    answer.sort(reverse=True)
    return answer

# yellow = a*b
# brown = 4 + 2a + 2b