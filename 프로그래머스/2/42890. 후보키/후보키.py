from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    
    # 조합으로 가능한 모든 인덱스 저장
    combi = []
    for i in range(1,col+1):
        combi.extend(combinations([n for n in range(0,col)],i))
    
    # 유일성
    unique = []
    for i in combi:
        tmp = [tuple(item[index] for index in i) for item in relation]
        
        if len(set(tmp)) == row:
            put = True
            
            for x in unique:
                if set(x).issubset(set(i)):  # 최소성
                    put = False
                    break
                    
            if put:
                unique.append(i)
            
    return len(unique)