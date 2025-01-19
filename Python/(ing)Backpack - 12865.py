# 12865 / Backpack

import sys

frame = sys.stdin.readline().split()
backpack = []
basket = 0
max_value = []

for i in range(int(frame[0])):

    backpack.append(sys.stdin.readline().split())

for i in range(int(frame[0])):

    sub = 0

    while basket < int(frame[1]):
        
        if basket + backpack[sub][0] < int(frame[1]):
            
            basket += backpack[sub][0]

        sub += 1
        





print(backpack[0][0])

