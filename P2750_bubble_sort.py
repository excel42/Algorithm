#입력받은 수 오름차순 정렬
N = int(input()) # 정렬할 수 개수
A = [0]*N #입력 저장 리스트 초기화

for i in range(N): #
    A[i] = int(input())
print("----정렬결과----")
for i in range(N-1):
    for j in range(N-1-i):
        if A[j] > A[j+1]:
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp

for i in range(N):
    print(A[i])
