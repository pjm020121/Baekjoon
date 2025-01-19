# 1931 / Meeting

import sys

count = int(sys.stdin.readline())       # 미팅개수 조회

# 미팅시간 조회 후 튜플로 묶어서 정수형으로 저장
meeting_room = [tuple(map(int, sys.stdin.readline().split()))for _ in range(count)]

meeting_room.sort(key=lambda x: (x[1], x[0]))       # 끝나는시간을 기준으로 정렬, 동률일경우 시작시간을 기준

possible_room = 0
cnt = 0

for start, end in meeting_room:     # 회의 시작시간과 전 회의 끝나는 시간 겹치지 않으면 추가

    if start >= possible_room:
        cnt += 1
        possible_room = end

print(cnt)


















