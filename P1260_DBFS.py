from collections import deque
N, M, Start = map(int, input().split()) #노드개수, 엣지개수, 시작점
A = [[] for _ in range(N+1)] #그래프 형태 리스트로 저장

for _ in range(M): #엣지 갯수만큼 반복해서 입력
    s,e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(N + 1): #노드 오름차순 정렬
    A[i].sort()

def DFS(v): #재귀함수 형태 DFS
    print(v, end=' ') #현재 노드 출력
    visited[v] = True #방문 노드 기록
    for i in A[v]: 
        if not visited[i]:
            DFS(i)

visited = [False] * (N+1) #DFS 실행 전 리스트 초기화
DFS(Start) #깊이 우선 탐색 시작

def BFS(v): # 큐 사용해 구현
    queue = deque() #큐 생성
    queue.append(v) # 시작 노드 큐에 추가
    visited[v] = True #방문 노드 처리
    while queue:
        now_Node = queue.popleft()  #큐에서 노드 꺼냄
        print(now_Node, end=' ') # 현재 노드 출력
        for i in A[now_Node]: # 연결된 노드들 중
            if not visited[i]: #아직 방문하지 않은 노드
                visited[i] = True # 방문 처리
                queue.append(i) #큐에 추가

print() 
visited = [False] * (N+1) #리스트 초기화
BFS(Start) # 너비우선 탐색 시작