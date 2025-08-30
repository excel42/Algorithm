#자료구조 - 투포인터
#'좋은 수' 구하기
import sys
input = sys.stdin.readline
N = int(input()) #수의 개수
Result = 0
A = list(map(int, input().split())) #수 데이터 저장 리스트
A.sort()

for k in range(N):
    find = A[k]
    i = 0
    j = N - 1
    while i < j: #투 포인터 알고리즘
        if A[i] + A[j] == find:
            if i != k and j !=k: #두 포인터 i,j가 k가 아닐 때
                Result += 1 #좋은 수 개수 1증가
                break
            elif i == k: #두 포인터 i와 k일치
                i += 1
            elif j == k: #두 포인터 i와 j일치
                j -= 1
        elif A[i] + A[j] < find: 
            i += 1 #포인터 i 증가
        else : 
            j -= 1 #포인터 j 감소

print(Result)