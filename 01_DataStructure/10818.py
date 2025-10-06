#Arraylist
#최소, 최대

n = int(input()) #숫자 개수 n
array_list = list(map(int, input().split())) #정수 n개 입력

max_num = array_list[0] #최대값
min_num = array_list[0] #최소값

for num in array_list: #for문으로 배열 순회

    if num > max_num: #현재값과 최대값 비교
        max_num = num
    if num < min_num: #현재값과 최소값 비교
        min_num = num

print(min_num, max_num) #최소 최대 출력