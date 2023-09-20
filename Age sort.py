# 10814 / Age sort

import sys

# 사람들 수 입력
count = int(sys.stdin.readline())

age = []    # 나이를 담을 리스트
name = []    # 이름을 담을 리스트
total = []    # 최종 리스트

# 입력받기
for i in range(count):

    info = sys.stdin.readline()
    info = info.split()
    age.append(info[0])
    name.append(info[1])

# 정렬하기
for i in range(count):

    head = 0
    k = 0

    while k <= len(age) - 1:

        if age[head] > age[k]:

            head = k

        k += 1

    total.append(age[head] + " " + name[head])
    age.pop(head)
    name.pop(head)

for i in range(len(total)):
    
    print(total[i])






