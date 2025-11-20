# 11866 / Yosepuse0

import sys

frame = sys.stdin.readline().split()    # 기초입력

count = int(frame[0])   # 사람 명 수
static_sequence = int(frame[1])     # 고정 정수
sequence = static_sequence - 1      # 탑으로 사용될 정수
result = []     # 최종 결과

yosepuse = [i + 1 for i in range(count)]    # 기초 숫자수열

while len(result) < count:  # count만큼 반복

    result.append(yosepuse[sequence])   # 최종 결과에 규칙에 맞는 수 배제
    yosepuse[sequence] = 0      # 선택된 수 0으로 초기화

    for i in range(static_sequence):    # 고정 정수만큼 반복

        sequence += 1   # 탑 이동

        if sequence > len(yosepuse) - 1:    # 탑이 수열보다 클 경우

            sequence = 0

        while yosepuse[sequence] == 0  and len(result) < count:     # 기본 수열이 0으로 초기화 되어 있는 경우

            sequence += 1

            if sequence > len(yosepuse) - 1:

                sequence = 0

# 출력문
print('<', end='')

for i in range(len(result) - 1):
    print(result[i], end = '')
    print(',', end = ' ')

print(result[len(result) - 1], end = '')
print('>')