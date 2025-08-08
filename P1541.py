#P1541 잃어버린 괄호
#그리디 알고리즘
answer = 0
A = list(map(str, input().split("-"))) #A라는 이름의 리스트, -기준 나누기

def mySum(i): #-로 나뉜 그룹들의 합 구하기
    sum = 0
    temp = str(i).split("+") #+로 나뉜 리스트 내 값 합산
    for i in temp:
        sum += int(i)
    return sum

for i in range(len(A)):
    temp = mySum(A[i])
    if i == 0: #가장 앞 데이터(는 양수)일때
        #맨 앞 데이터가 음수 일 경우 첫 항은 null이 되어 오류
        answer += temp #결괏값 더하기
    else:
        answer -= temp #결괏값 빼기
    
print(answer)
