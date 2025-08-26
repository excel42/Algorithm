#이진트리
#트리 순회
import sys
input = sys.stdin.readline
N = int(input()) #노드 개수 입력
tree = {} #딕셔너리 형태 트리

for _ in range(N):
    root, left, right = input().split() #루트, 왼쪽, 오른쪽 데이터 입력
    tree[root] = [left, right] #tree 딕셔너리에 데이터 저장

#전위 순회(현-왼-오)
def preOrder(now): 
    if now == '.':
        return #자식 노드가 없는 경우
    print(now, end='')
    preOrder(tree[now][0]) #왼쪽 탐색
    preOrder(tree[now][1]) #오른쪽 탐색
#중위 순회(왼-현-오)
def inOrder(now):
    if now == '.':
        return
    inOrder(tree[now][0])
    print(now, end='')
    inOrder(tree[now][1])
#후위 순회(왼-오-현)
def postOrder(now):
    if now == '.':
        return
    postOrder(tree[now][0])
    postOrder(tree[now][1])
    print(now, end='')

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')