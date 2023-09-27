# 25918 / Polar_Bear

import sys

N = int(sys.stdin.readline())    # 문자열 길이
s = sys.stdin.readline()  # 문자열 입력

string = [None] * N

for i in range(N):

    string[i] = s[i]

O = 0    # 열린괄호 횟수
day = 1    # 걸린 날짜
plus_day = 1    # 추가 날짜
min_day = -1

# 날짜 분석
for i in range(len(s)):

    if s[i] == '(':

        O += 1

    elif s[i] == ')':

        O -= 1

    # O가 - 상태일 때 비교해줄 변수
    plus_O = +abs(O)

    # 괄호 안에 O의 수를 계산해서 날짜추가
    if O > plus_day:

        plus_day += 1
        day += 1

    # 괄호 안에 X의 수를 계산해서 날짜추가
    if O < min_day:

        if plus_O > plus_day:

            min_day -= 1
            plus_day += 1
            day += 1

# 괄호가 다 닫히지 않았을 때
if O != 0:

    day = -1

print(day)


