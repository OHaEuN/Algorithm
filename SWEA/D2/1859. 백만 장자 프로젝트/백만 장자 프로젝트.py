
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr=list(map(int,input().split()))
    answer = 0
    while len(arr) > 0:
        m = max(arr)
        m_index = arr.index(m)
        if m_index == n-1:
            for i in arr:
                answer+=m-i
                arr = []
        else:
            for i in range(m_index):
                answer+=m-arr[i]
            arr = arr[m_index+1:]
    
    print("#",end='')
    print(test_case,end=' ')
    print(answer)
    
