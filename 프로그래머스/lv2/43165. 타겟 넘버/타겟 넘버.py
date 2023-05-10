def solution(numbers, target):
    count = 0
    idx = 0
    n = 0
    def bfs(n,idx):
        nonlocal count
        if idx == len(numbers) and n == target:
            count +=1
        elif idx < len(numbers):
            bfs(n+numbers[idx],idx+1)
            bfs(n-numbers[idx],idx+1)  
    bfs(n,idx)

    return count
