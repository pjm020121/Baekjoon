# 2751 / Sort2

import sys

num = int(sys.stdin.readline().strip())     # 개행문자 제거하여 한 줄씩 입력
sequence = set()    # 중복방지 세트로 선언

for i in range(num):    # 개행문자 제거하여 입력받은 줄 하나씩 세트에 추가
    sequence.add(int(sys.stdin.readline().strip()))

sequence = sorted(sequence)     # 정렬

for i in range(len(sequence)):
    print(sequence[i])
