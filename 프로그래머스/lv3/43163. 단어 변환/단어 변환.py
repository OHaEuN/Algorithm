import sys
sys.setrecursionlimit(10**7)

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = set()  # 방문한 단어를 저장하기 위해 집합(set)으로 변경
    answer = []
    
    def bfs(word, count):
        if word == target:
            answer.append(count)
            return
        
        for another in words:
            if another not in visited:
                same = 0
                for i in range(len(word)):
                    if word[i] == another[i]:
                        same += 1
                if same == len(word) - 1:
                    visited.add(another)
                    bfs(another, count + 1)
                    visited.remove(another)  # 재귀 탐색이 끝난 후 방문 기록을 제거하여 다른 경로에서 방문할 수 있도록 함
    
    bfs(begin, 0)
    
    if answer:
        return min(answer)
    else:
        return 0