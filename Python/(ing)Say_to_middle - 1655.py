# 1655 / Say_to_middle

import sys

count = int(sys.stdin.readline())
integer = list()
temp = list()

for i in range(count):

    integer.append(int(sys.stdin.readline()))
    integer.sort()

    if len(integer) % 2 == 0:
        
        temp.append(integer[(len(integer) // 2) - 1])

    elif len(integer) % 2 == 1:
        
        temp.append(integer[(len(integer) // 2)])


for i in temp:
    print(i)
