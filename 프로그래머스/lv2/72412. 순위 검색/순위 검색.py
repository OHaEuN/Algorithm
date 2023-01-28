from collections import defaultdict
from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    infos = defaultdict(list)
    answer=[]
    # 입력값 파싱 후 리스트에 담음
    for q in range(0,len(query)):
        query[q] = query[q].split(' ')
        query[q] = [i for i in query[q] if i !='and']
    for i in range(0,len(info)):
        info[i] = info[i].split(' ')
    
    for i in info:
        conditions =i[:-1]
        score =int(i[-1])
        for r in range(5):
            combis = list(combinations(range(4),r)) # '-'로 바꿀 위치의 경우의 수
            
            for c in combis:
                test_cases = conditions[:]
                for v in c:
                    test_cases[v] = '-'
                
                infos['_'.join(test_cases)].append(score)
    for item in infos:
        infos[item].sort()
    # print(infos)
    
    for q in query:
        conditions = '_'.join(q[:-1])
        score = int(q[-1])
        
        count=0
        if conditions in infos:
            data = infos[conditions]
            idx = bisect_left(data, score)
            count = len(data) - idx
            # if len(data)>0:
            #     start, end = 0, len(data)
            #     while start != end and start != len(data):
            #         if data[(start+end)//2]>=score:
            #             end = (start+end)//2
            #         else:
            #             start=(start+end)//2+1
            #     answer.append(len(data)-start)
            # else:
            #     answer.append(0)
        answer.append(count)
    
        
        
        #     효율성 통과 못한 풀이
#     count=0
#     answer = [0 for i in range(len(query))]
    
#     for i in info:
#         for q in range(0,len(query)):
#             if int(i[4]) >= int(query[q][4]):
#                 for n in range(0,4):
#                     if query[q][n] == '-' or i[n]==query[q][n]:
#                         count+=1
#             if count == 4:
#                 answer[q]+=1
#             count = 0
    
    return answer