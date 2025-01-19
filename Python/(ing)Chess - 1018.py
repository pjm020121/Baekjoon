# 1018 / Chess

import sys

bord = sys.stdin.readline()
bord = bord.split()
bord = [int(i) for i in bord]
width = 0
height = 0
i = 0

chess = []

for i in range(bord[0]):

    square = sys.stdin.readline()
    chess.append(square)

while len(chess) > 8:

    chess.pop(width)

    if width == 0:

        width = len(chess) - 1

    elif width == len(chess) - 1:

        width = 0

while len(chess[i]) > 9:

    

    if height == 0:

        height = len(chess[i]) - 2

    elif height == len(chess[i]) - 2:

        height = 0


print(chess)







