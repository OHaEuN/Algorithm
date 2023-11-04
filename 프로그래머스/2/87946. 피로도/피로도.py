from itertools import permutations
def solution(k, dungeons):
    answer = 0
    dungeons_list = list(permutations(dungeons, len(dungeons)))
    temp = k
    for dungeon in dungeons_list:
        k = temp
        count = 0
        for dg in dungeon:
            if k >= dg[0]:
                if k >= dg[1]:
                    k -= dg[-1]
                    count +=1
                    
        answer = max(answer,count)
    return answer