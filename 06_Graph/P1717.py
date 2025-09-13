#Union Find
#P1717_집합의 표현
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000) #질의 개수 최대 백만
N, M = map(int, input().split())
parent = [0] * (N + 1) #대표 노드 저장 리스트

def find(a): #find 연산
    if a == parent[a]: #a가 대표 노드면 리턴
        return a
    else:
        parent[a] = find(parent[a]) #아닐 경우 대표 노드값을 find(parent[a])값으로 저장
        return parent[a] #재귀함수
    
def union(a, b): #Union 연산
    a = find(a) 
    b = find(b)
    if a != b:
        parent[b] = a #두 원소 대표 노드끼리 연결

def checkSame(a, b): #두 원소가 같은 집합인지 확인
    a = find(a)
    b = find(b)
    if a == b: #두 대표 노드가 같으면 참
        return True
    return False #아니면 거짓

for i in range(0, N+1):
    parent[i] = i #대표 노드를 자기 자신으로 초기화

for i in range(M):
    question, a, b = map(int, input().split())
    if question == 0: #질의가 0이면
        union(a,b) #집합 합치기
    else:
        if checkSame(a,b): #같은 집합 원소인지 확인하고 결과값 출력
            print("YES")
        else:
            print("NO")
