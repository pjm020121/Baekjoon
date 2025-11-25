# 1966 / Printer_Queue

import sys
from collections import deque

# 테스트 케이스의 수 입력
Testcase_num = int(sys.stdin.readline().strip())

for i in range(Testcase_num):

    testcase, priority = list(map(int, sys.stdin.readline().split()))           # 테스트 케이스 길이와 원하는 priority입력
    Printer_Queue = deque(map(int, sys.stdin.readline().split()))               # 각 공백을 기준으로 문자열을 정수로 입력받아 deque에 저장
    Printer_Queue = deque((n, m) for n, m in enumerate(Printer_Queue))          # 각 원소에 enumerate를 통해 인덱스부여
    count = 0

    # 테스트 케이스 내 원소가 1개인 경우
    if testcase == 1:

        print(1)

    # 테스트 케이스 내 원소가 다수인 경우
    elif testcase > 1:

        # Printer_Queue 내 데이터가 없어질 때까지 반복
        while Printer_Queue:

            # 첫번째 원소 추출
            idx, pr = Printer_Queue.popleft()

            # 해당 원소보다 큰 원소 discovery시 추출했던 원소 가장 후순위로 추가
            if any(pr < MAX for _, MAX in Printer_Queue):
                Printer_Queue.append((idx, pr))

            # 추출 원소가 가장높은 우선순위를 가질경우 카운팅 후 해당 원소가 원했던 priority라면 break
            else:
                count += 1
                if idx == priority:
                    print(count)
                    break
