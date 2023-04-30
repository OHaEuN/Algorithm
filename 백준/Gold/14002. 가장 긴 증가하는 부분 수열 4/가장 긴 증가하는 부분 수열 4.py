# 수열 A의 크기 N 입력 받기
n = int(input())

# 수열 A 입력 받기
a = list(map(int, input().split()))

# 각 위치에서 끝나는 LIS의 길이를 저장할 리스트 dp 초기화
dp = [1] * n

# 각 위치에서 끝나는 LIS의 이전 항목을 저장할 리스트 prev 초기화
prev = [-1] * n

# 가장 긴 LIS의 길이와 그 위치를 저장할 변수 초기화
lis_len = 1
lis_end = 0

# 각 위치에서 끝나는 LIS의 길이와 이전 항목을 dp와 prev에 저장하면서 가장 긴 LIS의 길이와 그 위치를 찾는다
for i in range(n):
    for j in range(i):
        if a[j] < a[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            prev[i] = j
    if dp[i] > lis_len:
        lis_len = dp[i]
        lis_end = i

# 가장 긴 LIS 출력하기
lis = []
while lis_end != -1:
    lis.append(a[lis_end])
    lis_end = prev[lis_end]
lis.reverse()

# 결과 출력하기
print(lis_len)
print(*lis)
