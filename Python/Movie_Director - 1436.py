# 1436 / Movie_Director

import sys

N = int(sys.stdin.readline())    # 영화 회차 수

The_end = 666    # 1번째 영화

# 666이 나올때마다 회차 수 감소하면서 연산
while True:

    if '666' in str(The_end):

        N -= 1

    if N <= 0:

        break

    The_end += 1

print(The_end)

