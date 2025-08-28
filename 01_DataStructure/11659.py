#DataStructure
#구간합 구하기
import sys
input = sys.stdin.readline
suNo, quizNo = map(int, input().split()) #숫자개수, 질의개수 입력
numbers = list(map(int, input().split())) # 숫자 데이터 입력
prefix_sum = [0] #합 배열

temp = 0 #변수 선언
for x in numbers:
    temp = temp +x #temp에 숫자 데이터 더해 주기
    prefix_sum.append(temp) #합 배열에 temp 값 저장

ans = []
for _ in range(quizNo):
    s, e = map(int, input().split()) #질의 범위 입력
    ans.append(str(prefix_sum[e] - prefix_sum[s-1])) #구간 합 출력

sys.stdout.write("\n".join(ans)) #마지막 출력