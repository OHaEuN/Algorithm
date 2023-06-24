def solution(files):
    answer =[]
    head = ''
    number = ''
    tail = ''
    for file in files:
        num_start = -1
        num_end = -1
        for i in range(len(file)):
            if file[i].isdigit():     # 숫자가 나오면 그 이전은 무조건 HEAD, 이후는 NUMBER, TAIL로 다시 구분
                head = file[:i]
                number = file[i:]
                
                for j in range(len(number)):    # NUMBER와 TAIL 구분 (숫자 안나오면 TAIL)
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break
                        
                answer.append([head, number, tail])
                head, number, tail = '', '', ''
                break
    answer = sorted(answer, key = lambda x: (str(x[0]).upper(),int(x[1])))
    
    return ([''.join(i) for i in answer])