# 1655 / Say_to_middle

import sys
import heapq

count = int(sys.stdin.readline())
max_heap, min_heap = list(), list()

# 최대 힙과 최소힙 사용, 최대힙의 루트를 중앙값으로 사용
for i in range(count):

    num = int(sys.stdin.readline())

    if not max_heap or num <= -max_heap[0]:

        heapq.heappush(max_heap, -num)

    else:

        heapq.heappush(min_heap, num)

    # 중앙값 재설정, 루트가 최대힙에 있기에 최소힙에 1을 더해줌
    if len(max_heap) > len(min_heap) + 1:

        heapq.heappush(min_heap, -heapq.heappop(max_heap))

    elif len(max_heap) < len(min_heap):

        heapq.heappush(max_heap, -heapq.heappop(min_heap))

    print(-max_heap[0])