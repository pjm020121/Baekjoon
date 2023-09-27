# 2839 / Sugar_Greedy

import sys

sugar = int(sys.stdin.readline())    # 설탕 kg받기

cnt = 0    # 봉지수

sugar_copy = sugar    # 설탕 초과수

if sugar >= 5:    # 만약 설탕이 5kg이상일 때

    cnt += sugar / 5
    sugar %= 5
    cnt = int(cnt)

    if sugar % 3 != 0 and sugar != 0:    # 만약남은 설탕이 3으로 나눠지지 않거나 0이 아니면

        while sugar % 3 != 0:

            cnt -= 1
            sugar += 5

            if cnt <= 0:
                sugar = sugar_copy
                break

    if sugar % 3 != 0 and sugar != 0:    # 남은 설탕이 3으로 나눠지지 않거나 0이 아니면

        cnt = 0
        sugar = sugar_copy

if sugar % 3 == 0 and sugar != 0:    # 남은 설탕이 3키로로 나눠질 때

    cnt += sugar / 3
    cnt = int(cnt)
    sugar %= 3

elif sugar % 3 != 0 and sugar != 0:    # 남은 설탕이 3키로보다 적거나 0이 아닐 때

    cnt = -1

print(cnt)
