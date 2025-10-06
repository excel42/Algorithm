#이진탐색(매개변수)탐색
#나무 자르기(절단기 설정 높이 최댓값)
from sys import stdin
input = stdin.readline

N, M = map(int, input().split()) #나무의 수, 나무의 길이
tree = list(map(int, input().split())) #가져갈 나무 순차 입력
start, end = 1, max(tree)

while start <= end:
    mid = (start + end) // 2
    tree_length = 0
    #나무 자르기
    for i in tree:
        if mid <= i:
            tree_length += i - mid
    #자른 나무가 충분하니, 높이를 올린다.
    if tree_length >= M:
        start = mid + 1
    #잘라진 나무가 부족하니, 높이를 내린다.
    else:
        end = mid - 1
print(end) #절단기 높이의 최댓값