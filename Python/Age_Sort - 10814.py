# 10814 / Age_Sort

import sys

# 사람들 수 입력
count = int(sys.stdin.readline().strip())

info = []

# 공백을 기준으로 각 변수에 저장하여 리스트에 튜플로 저장
for i in range(count):

    age, name = sys.stdin.readline().split()
    info.append((int(age), name))

# 람다로 info리스트 내 튜플의 0번째 요소를 기준으로 정렬
info.sort(key=lambda x : x[0])

for i in range(len(info)):
    print(info[i][0], end = " ")
    print(info[i][1])




