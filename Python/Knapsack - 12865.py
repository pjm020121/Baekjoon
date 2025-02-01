# 12865 / Knapsack

import sys

# 무게와 가치 입력
count, limit = map(int, sys.stdin.readline().split())
weight, value = list(), list()
dp = [0] * (limit + 1) 

# 각 리스트에 할당
for i in range(count):

    w, v = map(int, sys.stdin.readline().split())
    weight.append(w)
    value.append(v)

# DP를 이용한 최적의 해 구하기
for i in range(count):
    for k in range(limit, weight[i] - 1, -1):
        dp[k] = max(dp[k], dp[k - weight[i]] + value[i])

print(dp[limit])

