# 10815 / Number_card

import sys

card = []   # 카드 더미
sample = []     # 보기 숫자들
agreement = []      # 일치, 불일치 여부

count = int(sys.stdin.readline())   # 카드 갯수
card = sys.stdin.readline().split()     # 카드 공백으로 분리

count = int(sys.stdin.readline())   # 위와 동일
sample = sys.stdin.readline().split()   # 위와 동일

card = set(card)    # 시간복잡도 O(1)을 가진 set로 변환

# 만약 샘플과 카드 더미숫자가 일치할경우 1 아닐 경우 0표시
for i in range(count):

    if sample[i] in card:
        agreement.append(1)

    else:
        agreement.append(0)

for i in range(len(agreement)):

    print(agreement[i], end = ' ')



