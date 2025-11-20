# 1764 / A person you've never heard of

import sys

def recur(list, tar, start, end):

    global final_list

    if start > end:
        return False

    mid = (start + end) // 2

    if list[mid] == tar:
        return True

    elif list[mid] > tar:
        return recur(list, tar, start, mid - 1)

    elif list[mid] < tar:
        return recur(list, tar, mid + 1, end)

if __name__ == "__main__":

    n, m = map(int, sys.stdin.readline().split())

    list = []
    final_list = []

    for i in range(n):

        list.append(sys.stdin.readline())

    list = sorted(list)

    for i in range(m):
        person = sys.stdin.readline()
        if recur(list, person, 0, n - 1):
            final_list.append(person)

    final_list = sorted(final_list)
    print(len(final_list))
    for i in final_list:
        print(i, end='')
