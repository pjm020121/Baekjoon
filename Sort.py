# 2750 / Sort

import sys

num = int(sys.stdin.readline())    # 사용할 정수 개수입력

list = []    # 정수를 담아둘 리스트

head = 0    # 크기를 비교할 정수

for i in range(num):    # 정수 입력받기

    count = int(sys.stdin.readline())

    list.append(count)

for i in range(len(list)):    # 정수를 비교하여 변경

    head = i

    for k in range(len(list)):

        if list[head] > list[k] and k > head:

            head = k

    temp = list[head]
    list[head] = list[i]
    list[i] = temp

for i in range(len(list)):    # 정수출력

    print(list[i])
