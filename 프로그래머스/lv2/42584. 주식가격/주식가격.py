def solution(prices):
    answer = []
    for i in range(len(prices)):
        temp = prices[i]
        cnt = 0
        for n in range(i,len(prices)-1):
            if prices[n] >= temp:
                cnt += 1
            else:
                break
        answer.append(cnt)
                
    return answer