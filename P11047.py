#P11047_동전개수최솟값구하기
#그리디 알고리즘

N,K = map(int, input().split())
A = [0] * N

for i in range(N):
    A[i] = int(input())

count = 0

for i in range(N-1, -1, -1):
    if A[i] <= K:
        count += int(K / A[i])
        K = K % A[i]
    
print(count)