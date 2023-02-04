def solution(files):
#     arr =[]
#     head, number, tail = '', '', ''
    
#     for item in files:
#         for i in range(0,len(item)):
#             if item[i].isdigit():
#                 head=item[:i]
#                 for j in range(i+1,len(item)):
#                     if not item[j].isdigit():
#                         number = item[i:j]
#                         tail = item[j:]
#                         arr.append([head, number, tail])
#                         break
#                 head, number, tail = '', '', ''
#                 break

#     arr = sorted(arr, key=lambda x:(x[0].lower(), int(x[1])))
    
#     return [''.join(i) for i in arr]
    tmp = []
    head, number, tail = '', '', ''
    
    for file in files:       
        for i in range(len(file)):
            if file[i].isdigit():     # 숫자가 나오면 그 이전은 무조건 HEAD, 이후는 NUMBER, TAIL로 다시 구분
                head = file[:i]
                number = file[i:]
                
                for j in range(len(number)):    # NUMBER와 TAIL 구분 (숫자 안나오면 TAIL)
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break
                        
                tmp.append([head, number, tail])
                head, number, tail = '', '', ''
                break

    tmp = sorted(tmp, key=lambda x:(x[0].lower(), int(x[1])))

    return [''.join(i) for i in tmp]