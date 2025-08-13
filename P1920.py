# P1920: 이진탐색
# https://www.acmicpc.net/problem/1920
N = int(input())
A = list(map(int, input().split()))
A.sort()#자동 정렬
M = int(input())
target_list = list(map(int, input().split()))

for i in range(M):
    find = False
    target = target_list[i]
    # 이진 탐색 시작
    start = 0
    end = len(A) - 1
    while start <= end:
        midi = int((start + end) / 2) #중간 인덱스
        midv = A[midi] #중앙값
        if midv > target: #중앙값이 타겟보다 클 때
            end = midi - 1 #왼쪽 이동
        elif midv < target: #중앙값이 타겟보다 작을 때
            start = midi + 1 #오른쪽 이동
        else:
            find = True #타깃 발견
            break #종료
    if find: #탐지 성공
        print(1)
    else: #탐지 실패
        print(0)