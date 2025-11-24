# 1966 / Printer_Queue

import sys
from collections import deque

Testcase_num = int(sys.stdin.readline().strip())

for i in range(Testcase_num):

    testcase = list(map(int, sys.stdin.readline().split()))
    Printer_Queue = deque(map(int, sys.stdin.readline().split()))
    Printer_Queue = deque((n, m) for n, m in enumerate(Printer_Queue))
    count = 0

    if testcase[0] == 1:

        print(1)

    elif testcase[0] > 1:

        while Printer_Queue:

            idx, pr = Printer_Queue.popleft()

            if any(pr < x for _, x in Printer_Queue):
                Printer_Queue.append((idx, pr))

            else:
                count += 1
                if idx == testcase[1]:
                    print(count)
                    break
