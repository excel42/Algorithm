# 타임머신으로 빨리 가기
# 벨만-포드 알고리즘

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
edges = [] #에지 정보 저장 리스트
distance = [sys.maxsize]*(N+1) #거리 리스트

for i in range(M): #에지 개수만큼 반복해, 에지 정보 저장
    start, end, time = map(int,input().split())
    edges.append((start, end, time))

#벨만-포드 수행
distance[1]=0 #출발 노드 0으로 초기화

for j in range(N-1):
    for start, end, time in edges:
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
            distance[end] = distance[start] + time #종료 노드값 = 출발노드값 + 에지 가중치

#음수 사이클 확인
mCycle = False

for start, end, time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
        mCycle = True #음수 사이클 존재

if not mCycle:
    for i in range(2, N+1):
        if distance[i] != sys.maxsize:
            print(distance[i]) #거리 리스트 출력
        else:
            print(-1) #음수 사이클 존재시

else:
    print(-1) #음수 사이클 존재시
