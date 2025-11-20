# 1018 / Chess

import sys

'''
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

<<<<<<< HEAD:Python/Chess - 1018.py



=======
>>>>>>> 00e7cacb3847a4509cd75185a83b99f2b161f463:Python/(ing)Chess - 1018.py
while len(chess[i]) > 9:

    

    if height == 0:

        height = len(chess[i]) - 2

    elif height == len(chess[i]) - 2:

        height = 0


print(chess)
'''


size = sys.stdin.readline().split()
size = [int(i) for i in size]
bord = [[None for _ in range(size[1])] for _ in range(size[0])]

print()

for i in range(size[0]):

    square = input()
    bord[i] = square

print(bord)



