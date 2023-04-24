def solution(priorities, location):
    temp = priorities[location]
    priorities[location] = 0
    cnt = 1
    while 1:
        Max= max(priorities)
        if temp > Max:
            Max = temp
        if priorities[0] == 0:
            if temp >= Max:
                return cnt
            else:
                priorities.append(priorities[0]) 
                priorities = priorities[1:]
        elif priorities[0] >=Max:
            cnt+=1
            priorities = priorities[1:]
        else:
            priorities.append(priorities[0]) 
            priorities = priorities[1:]
            
    return answer