def solution(sizes):
    a,b=0,0
    for s in sizes:
        A,B = sorted(s)
        a = max(a,A)
        b = max(b,B)
    return a*b
    
    # 일단 앞에 더 큰 수가 오게 정렬
    # 첫번째 요소 중의 최대, 두번째요소 중의 최대를 곱한 값
    