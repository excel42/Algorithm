import sys
input = sys.stdin.readline
n, m = map(int, input().split())
textList = set([input() for _ in range(n)]) #set 형태로 집합 S문자열 저장
count = 0

for _ in range(m): #set형태의 집합 문자열에서 검사 문자열이 있는지 확인
    subText = input()
    if subText in textList:
        count +=1

print(count)