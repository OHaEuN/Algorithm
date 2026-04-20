def solution(progresses, speeds):
    answer = []
    days = []
    for p,s in zip(progresses,speeds):
        day = (100-p)//s
        if (100-p)%s>0:
            day+=1
        days.append(day)
    
    m = 0
    for d in days:
        if (d > m):
            answer.append(1)
            m = d
        else:
            answer[-1] += 1
            
    return answer