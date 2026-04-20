def solution(numbers, target):
    temp = [0]
    for n in numbers:
        arr = []
        for t in temp:
            arr.append(t+n)
            arr.append(t-n)
        temp = arr
        
    answer = 0
    for t in temp:
        if t == target:
            answer +=1
        
    return answer


