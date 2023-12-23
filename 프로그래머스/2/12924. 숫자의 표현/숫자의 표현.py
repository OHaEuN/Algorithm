def solution(n):
    answer = 1
    s,e =1,2
    
    # 범위 내 수들의 합
    def range_sum(s,e):
        num = 0
        for i in range(s,e+1):
            num += i
        return num
    
    # 합이 작을 경우 e+=1, 합이 클 경우 s+=1
    while s<n and e<n and s<e:
        sum_result = range_sum(s,e)
        if sum_result < n:
            e += 1
        elif sum_result > n:
            s += 1
        elif sum_result == n:
            answer+=1
            e += 1
        
    return answer