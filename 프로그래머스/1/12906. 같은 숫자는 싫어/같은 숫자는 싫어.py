def solution(arr):
    q = []
    temp = 10
    for i in arr:
        if i != temp:
            q.append(i)
            temp = i
    return q