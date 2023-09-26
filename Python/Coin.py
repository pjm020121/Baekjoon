# 11047 / Coin

import sys

coin_list = []    # 동전의 단위를 적어둘 리스트
cnt = 0    # 동전의 개수

value = sys.stdin.readline()    # 동전의 값과 개수 입력받기
value = value.split()
value = [int(i) for i in value]

for i in range(value[0]):    # 동전의 단위 리스트 입력받기

    coin = int(sys.stdin.readline())
    coin_list.append(coin)

value = value[1]    # 값만을 할당

for i in range(len(coin_list)):    # 만약 값이 coin_list보다 클 경우 빼주는 for문

    if value >= coin_list[len(coin_list) - (i + 1)]:    # 가장 큰 값부터 비교

        cnt += value / coin_list[len(coin_list) - (i + 1)]
        value %= coin_list[len(coin_list) - (i + 1)]
        cnt = int(cnt)

print(cnt)
