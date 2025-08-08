#P11047_동전개수최솟값구하기
#그리디 알고리즘

N,K = map(int, input().split()) #N(동전개수),K(목표금액)
A = [0] * N #동전 데이터

for i in range(N): #동전을 리스트에 저장
    A[i] = int(input())

count = 0

for i in range(N-1, -1, -1): #가치가 큰 동전부터 역순으로
    if A[i] <= K: #목표 금액보다 동전 가치가 이하이면
        count += int(K / A[i]) #동전 수 += 목표금액 / 현재동전가치
        K = K % A[i] #목표 금액 = 목표금액 % 현재동전가치
    
print(count) #누적된 동전 수 출력