# 11399 / ATM

import sys

human = int(sys.stdin.readline())    # 사람 수 입력받기

total_minute = 0    # 총 걸린 시간

min = 0    # 최소값
min_recursive = 0    # 최소값을 하나씩 담아둘 재귀변수

minute = sys.stdin.readline()    # 걸리는 시간
minute = minute.split()    # 띄어쓰기 분리
minute = [int(i) for i in minute]    # 정수로 형변환

for i in range(len(minute)):    # 정렬하는 사람 수

    min = i    # 최소값을 구하고 배재하기 위함

    for k in range(len(minute)):    # 최소값 정렬

        if minute[min] > minute[k] and k > min:

            temp = minute[min]
            minute[min] = minute[k]
            minute[k] = temp

    total_minute += min_recursive + minute[min]    # total값 추가
    min_recursive += minute[min]    # 추가되는 분 재귀로 표현

print(total_minute)