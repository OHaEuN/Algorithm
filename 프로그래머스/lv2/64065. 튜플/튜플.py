def solution(s):
    sen = s.replace('{','').replace('}','')
    nums =list(map(int,sen.split(',')))
    setnums =list(map(int,set(sen.split(','))))
    arr =[]
    answer =[]
    for i in setnums:
        arr.append([nums.count(i),i])
    arr.sort(reverse=True)
    for num,i in arr:
        answer.append(i)
    return answer