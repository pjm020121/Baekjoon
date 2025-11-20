# 1463 / Make_to_one

import sys

value = int(sys.stdin.readline())
arr = [0, 0, 1, 1]

if value >= 4:
    for i in range(4, value + 1):
        v1 = 1 + arr[i - 1]
        v2 = 1 + arr[i - 1]
        v3 = 1 + arr[i - 1]

        if i % 3 == 0:
            v1 = 1 + arr[i // 3]

        if i % 2 == 0:
            v2 = 1 + arr[i // 2]

        arr.append(min(v1, v2, v3))

print(arr[value])

