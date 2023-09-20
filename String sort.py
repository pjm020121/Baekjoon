# 1181 / String sort

import sys

# 문자열 개수 입력
count = int(sys.stdin.readline())

str_list = []    # 문자열을 받을 리스트
sort_list = []    # 정렬된 문자열을 받을 리스트

# 문자열 입력받기
for i in range(count):

    string = sys.stdin.readline()
    str_list.append(string)

# lambda함수와 sorted를 이용해서 문자열 길이에 따라 정렬하기
str_list = sorted(str_list, key=lambda x : (len(x), x))

# 중복문자열 제거
for i in str_list:
    if i not in sort_list:
        sort_list.append(i)

for i in range(len(sort_list)):

    print(sort_list[i], end="")


