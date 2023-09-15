# 1931 / Meeting

import sys

meeting = int(sys.stdin.readline())    # 미팅 타임 입력

room = []    # 미팅시간 리스트
possible_room = []    # 가능한 시간대 리스트
cnt = 0    # 가능한 미팅룸 개수
k = 0    # 겹치는 시간대 확인할 변수
cnt_list = []

for i in range(meeting):    # 미팅시간 입력

    time = sys.stdin.readline()
    time = time.split()
    time = [int(i) for i in time]
    room.append(time)

for s in range(meeting):    # 기준 시간대 선정

    start = room[s]  # 기준 시간대

    possible_room.append(start)  # 기준 시간대 추가

    for i in range(len(room)):  # 가능한 시간대 찾는 for문

        start_time = room[i][0]  # 미팅 시작 시간대 확인
        end_time = room[i][1]  # 끝나는 시간 확인

        while True:  # 시간대 확인

            # 시작 시간과 끝나는 시간이 기준 시간들보다 크면 추가
            if possible_room[k][0] < start_time and possible_room[k][1] <= start_time:

                k += 1

            # 시작 시간과 끝나는 시간이 기준 시간들보다 작으면 추가
            elif possible_room[k][0] > start_time and possible_room[k][0] >= end_time:

                k += 1

            # 아니면 탈출
            else:

                break

            # 가능 시간대 리스트의 모든 시간과 겹치지 않으면 회의실 추가하고 횟수 + 1
            if k >= len(possible_room):
                cnt += 1
                possible_room.append(room[i])
                break

    cnt_list.append(cnt)    # 최종 회의실 가능 횟수 확인
    cnt = 0
    possible_room = []
    k = 0

cnt_list.sort()
if cnt_list[0] <= 0:

    cnt_list[0] = 1

print(cnt_list[len(cnt_list) - 1])























