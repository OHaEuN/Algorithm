import sys
input = sys.stdin.readline

N = int(input())

def moo(mooLength, current, N):
    prevLength = (mooLength - current)//2
    if N <= prevLength: # current 기준 앞쪽일때
        return moo(prevLength, current-1, N)
    elif N > prevLength + current: # current 기준 뒤쪽일때
        return moo(prevLength, current-1, N - prevLength - current) # 앞 뒤 대칭이니까 앞쪽 같은 위치로 옮겨서 다시 재귀
    else: # 가운데일때 맨 앞글자면 m 아니면 o 출력
        if N == prevLength + 1:
            return "m"
        else:
            return "o"


# n에 따른 moo 문장의 길이가 N보다 큰 최소값 구하기
mooLen, n = 3, 0
while N > mooLen :
    n +=1
    mooLen = mooLen*2 + n+3

print(moo(mooLen, n+3, N ))