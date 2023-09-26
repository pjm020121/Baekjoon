# 1874 / Stack_Sequence

import sys

count = int(sys.stdin.readline())    # 갯수 입력받기

stack = [0] * (count + 1)    # 수열 담을 리스트

for i in range(count + 1):    # 수 초기화
    stack[i] = i

top = 0

push_pop = []

# 수열 계산법
for i in range(count):

    n = int(sys.stdin.readline())

    while stack[top] < n:
        top += 1
        push_pop.append('+')

    if stack[top] >= n:

        if (stack[top] != n):
            push_pop = []
            push_pop.append("NO")
            break

        top -= 1
        stack.pop(top + 1)
        push_pop.append('-')

for i in range(len(push_pop)):
    print(push_pop[i])