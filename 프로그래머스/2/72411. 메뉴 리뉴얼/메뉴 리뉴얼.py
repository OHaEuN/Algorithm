from itertools import combinations
def solution(orders, course):
    answer = []
    for c in course:
        order_dic = {}
        for order in orders:
            order = sorted(list(order))
            if len(order)>=c:
                # combinations 한 다음에 order_dic 후보에 append
                o_combi = list(combinations(order,c))
                for o in o_combi:
                    order_dic[o] = order_dic.get(o,0) + 1
        if order_dic:
            max_count = max(order_dic.values())
            if max_count>=2:
                for k in order_dic:
                    if order_dic[k] == max_count:
                        answer.append(''.join(k))
        
    answer.sort() 
    return answer