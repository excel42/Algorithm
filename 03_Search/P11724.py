#연결 요소 구하기
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n,m = map(int, input().split()) #노드 개수, 엣지 개수(만큼 입력)
A = [[]for _ in range(n+1)] #그래프 데이터 저장 인접 리스트 초기화
visited = [False] * (n+1) #방문 기록 리스트 초기화

#DFS 구현
def DFS(v): 
    visited[v] = True #현재 노드 방문 기록
    for i in A[v]:
        if not visited[i]: #방문하지 않았다면 DFS 실행
            DFS(i)

#그래프 형태 입력
for _ in range(m): #m의 개수만큼 반복
    s, e = map(int, input().split()) #인접 리스트에 그래프 데이터 저장
    A[s].append(e)
    A[e].append(s)

#리스트에서 연결요소 세기
count = 0
for i in range(1, n+1): #n의 개수만큼 반복
    if not visited[i]: #방문하지 않은 요소가 있으면
        count += 1 #연결 개수 값 1 증가
        DFS(i) #DFS 실행

print(count)