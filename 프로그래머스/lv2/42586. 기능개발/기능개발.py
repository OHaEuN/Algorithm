import math
def solution(progresses, speeds):
    answer = []
    max = math.ceil((100-progresses[0])/speeds[0])
    cnt = 1
    for i in range(1,len(speeds)):
        temp = math.ceil((100-progresses[i])/speeds[i])
        if temp > max:
            answer.append(cnt)
            max = temp
            cnt = 1
        else:
            cnt +=1
        if i == len(speeds)-1:
            answer.append(cnt)
    return answer