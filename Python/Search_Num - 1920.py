# 1920 / Search_Num

import sys

count = int(sys.stdin.readline())    # 개수 입력

list = sys.stdin.readline().split()    # 숫자 입력

# 입력한 정수 갯수가 제한 입력 갯수보다 많으면 종료
if len(list) > count:
    sys.exit()

count2 = int(sys.stdin.readline())    # 2번째

list2 = sys.stdin.readline().split()    # 2번째

# 2번째
if len(list2) > count2:
    sys.exit()

# 세트로 변환
list_set = set(list)

# 비교
for i in range(len(list2)):

    if list2[i] in list_set:

        print(1)

    else:

        print(0)