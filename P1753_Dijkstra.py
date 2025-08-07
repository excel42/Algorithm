import sys
input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split()) #노드, 엣지 개수 입력
K = int(input()) # 출발 노드 입력
distance = [sys.maxsize] * (V + 1) # 거리 저장 리스트
visited = [False] * (V + 1) # 방문 여부 저장 리스트
myList = [[] for _ in range(V + 1)] # 에지 데이터 저장 인접 리스트
q = PriorityQueue() # 다익스트라 우선순위 큐

for _ in range(E): #인접 리스트에 에지 정보 저장
    u, v, w = map(int, input().split())
    myList[u].append((v, w))

q.put((0, K)) #출발 노드를 우선순위 큐에 넣고 시작
distance[K] = 0 # 거리 리스트에 출발 노드 값 0으로 설정

while q.qsize() > 0: 
    current = q.get() # 우선순위 큐에서 노드 가져오기
    c_v = current[1]
    if visited[c_v]: #방문여부 확인
        continue
    visited[c_v] = True
    for tmp in myList[c_v]: #  
        next_v, weight = tmp
        if distance[next_v] > distance[c_v] + weight:
            distance[next_v] = distance[c_v] + weight
            q.put((distance[next_v], next_v))
    
for i in range(1, V + 1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")