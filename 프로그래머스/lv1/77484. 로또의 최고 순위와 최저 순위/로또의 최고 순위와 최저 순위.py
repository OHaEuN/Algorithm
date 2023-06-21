def solution(lottos, win_nums):
    answer = []
    count = 0
    cnt0 = 0
    for l in lottos:
        if l in win_nums:
            count += 1
        elif l == 0:
            cnt0 += 1
    cnt_max = count+cnt0
    cnt_min = count
    
    def lotto(num):
        if num == 6:
            answer.append(1)
        elif num == 5:
            answer.append(2)
        elif num == 4:
            answer.append(3)
        elif num == 3:
            answer.append(4)
        elif num == 2:
            answer.append(5)
        else:
            answer.append(6)
    lotto(cnt_max)
    lotto(cnt_min)
    
    return answer