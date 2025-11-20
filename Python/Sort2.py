# 2751 / Sort2

import sys
count = sys.stdin.readline()
dic = {}

for i in range(int(count)):
    value = input()
    dic.setdefault(value, []).append(i)

list = sorted(dic)

for i in list:
    print(i)