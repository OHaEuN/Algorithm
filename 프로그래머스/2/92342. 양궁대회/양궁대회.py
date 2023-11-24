from itertools import combinations_with_replacement
def solution(n, info):
    answer = [-1]
    max_gap = -1
    for combi in combinations_with_replacement(range(11),n):
        lion = [0]*11
        for i in combi:
            lion[10-i]+=1
        L,A=0,0
        for i in range(11):
            if info[i]==lion[i]==0:
                continue
            elif info[i]>=lion[i]:
                A+=10-i
            else:
                L+=10-i
        if L > A:
            gap = L-A
            if gap > max_gap:
                max_gap = gap
                answer = lion
                
    return answer


