from collections import defaultdict

def solution(n, lost, reserve):
    students = defaultdict(int)
    for i in range(1,n+1):
        students[i] = 1
    for r in reserve:
        if r not in lost:
            students[r] += 1
        
    lost.sort()
    for l in lost:
        if l not in reserve:
            if students[l-1] == 2:
                students[l-1] = 1
            elif students[l+1] == 2:
                students[l+1] = 1
            else:
                students[l] = 0
    
    answer = 0
    for i in range(1,n+1):
        if students[i] >= 1:
            answer +=1
    return answer        

# n명의 학생을 값 1로 dict에 저장
# reserve인 학생이면 2
# lost 학생을 순회하면서 앞뒤 학생의 count가 2라면 빌리기