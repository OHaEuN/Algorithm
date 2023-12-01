from itertools import permutations
def solution(picks, minerals):
    answer = 0
    minerals_count = [[0,0,0] for _ in range(10)]
    if sum(picks)*5 < len(minerals):
        minerals = minerals[:5*sum(picks)]
    
    # 5개씩 잘라 피로도 높은 광물 그룹이 우선되게 정렬
    for i in range(len(minerals)):
        m = minerals[i]
        if m == "diamond":
            minerals_count[i//5][0] +=1
        elif m == "iron":
            minerals_count[i//5][1] +=1
        elif m == "stone":
            minerals_count[i//5][2] +=1
    minerals_count.sort(key = lambda x : (-x[0],-x[1],-x[2]))
    
    # picks에서 순서대로 쓰면서 피로도 계산
    for M in minerals_count:
        if picks[0]>0:
            picks[0]-=1
            answer += M[0]+M[1]+M[2]
        elif picks[1]>0:
            picks[1]-=1
            answer += 5*M[0]+M[1]+M[2]
        elif picks[2]>0:
            picks[2]-=1
            answer += 25*M[0]+5*M[1]+M[2]            
    
    return answer