#K번째 최단경로 찾기
#Dijkstra 알고리즘을 이용하여 K번째 최단경로를 찾는 문제

import sys
import heapq
input = sys.stdin.readline
N, M, K = map(int, input().split())  # 노드 개수, 엣지 개수, K번째 최단경로
W = [[] for _ in range(N + 1)]  # 그래프 초기화
distance = [[sys.maxsize] * (K) for _ in range(N + 1)]  # 거리 초기화

for _ in range(M):  # 엣지 입력
    a,b,c = map(int, input().split())
    W[a].append((b, c))  # 방향 그래프

pq = [(0, 1)] #가중치 우선, 가중치>목표노드 순으로 저장
distance[1][0] = 0  # 시작 노드의 거리 초기화

while pq:  # 변형 다익스트라 수행
    cost, node = heapq.heappop(pq)  # 현재 노드와 비용
    for nNode, nCost in W[node]:
        sCost = cost + nCost  # 현재 노드에서 다음 노드까지의 비용
        if distance[nNode][K - 1] > sCost:
            distance[nNode][K - 1] = sCost
            distance[nNode].sort()
            heapq.heappush(pq, (sCost, nNode))

for i in range(1, N + 1):  # 결과 출력
    if distance[i][K - 1] == sys.maxsize:
        print(-1)  # K번째 최단경로가 없는 경우
    else:
        print(distance[i][K - 1])  # K번째 최단경로 출력