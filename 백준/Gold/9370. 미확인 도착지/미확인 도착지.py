import sys
import heapq
input = sys.stdin.readline
INF = float('inf')


def dijkstra(start):
    q = []

    # (출발점에서의 거리, g-h 도로를 지났는지에 대한 플래그, 현재 노드)
    # 플래그가 0일 경우 -> g-h 도로를 지나지 않음, 플래그가 -1일 경우 -> g-h 도로를 지남
    heapq.heappush(q, (0, 0, start)) 

    while q:
        dist, ghFlag, now = heapq.heappop(q)

        # 출발점에서의 거리가 같을 경우 플래그가 -1인(g-h 도로를 지나는 경로)가 먼저 힙에서 꺼내지기 때문에
        # distance[now]와 dist가 같은 경우도 continue를 해준다.
        if distance[now] <= dist: 
            continue
        
        # 출발점에서 now까지의 거리와 g-h 도로를 지났는지에 대한 기록을 해준다.
        distance[now] = dist
        includeGH[now] = ghFlag

        for (next, nextDist) in roads[now]:
            cost = dist + nextDist
            
            # 보통 다익스트라는 <를 통해 비교하지만 해당 문제는 특정 도로를 지났는지를 판단해야 한다.
            # 그렇기 때문에 거리가 같은 경우도 힙에 넣어주도록 <= 비교 연산자를 사용한다.
            # 예를 들어, 처음에는 g-h 도로를 지나지 않은 거리가 7인 경로를 힙에 넣었는데
            # 추후에 g-h 도로를 지난 거리가 7인 경로를 찾을 수 있다.
            if cost <= distance[next]:
                # g-h 도로를 지났을 경우 플래그를 -1로 설정하여 힙에 넣어준다.
                if (now, next) == (g, h) or (now, next) == (h, g):
                    heapq.heappush(q, (cost, -1, next))
                else: # 그렇지 않을 경우 기존의 플래그 값을 넣어준다.
                    heapq.heappush(q, (cost, ghFlag, next))



T = int(input())
for _ in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    roads = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    includeGH = [0] * (n+1) # 최소 경로가 g-h 도로를 지났는지 여부. -1이면 지났음을 뜻한다.
    destinations = set() 

    for _ in range(m):
        a, b, d = map(int, input().split())
        roads[a].append((b, d))
        roads[b].append((a, d))

    for _ in range(t):
            destinations.add(int(input()))

    dijkstra(s)

    # g-h 도로를 지나는 최소 경로를 가진 도시들을 trueIncludeGH 셋에 넣어준다.
    # 그 후 목적지 후보 set과 교집합 연산을 통해서 문제의 답을 구한다.
    trueIncludeGH = set([x for x in range(n+1) if includeGH[x] == -1])
    resList = sorted(list(destinations.intersection(trueIncludeGH)))


    for res in resList:
        print(res, end=' ')
    print()
