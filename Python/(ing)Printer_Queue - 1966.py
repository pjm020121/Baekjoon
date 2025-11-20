import sys

Testcase_num = int(sys.stdin.readline())

for i in range(Testcase_num):

    testcase = list(map(int, sys.stdin.readline().split()))
    Printer_Queue = list(map(int, sys.stdin.readline().split()))
    pointer = -1
    count = 0

    if testcase[0] == 1:

        print(1)

    elif testcase[0] > 1:

        for k in range(testcase[0]):

            if pointer == testcase[1]:
                break

            count += 1

            pointer = (pointer + 1) % len(Printer_Queue)

            if Printer_Queue[pointer] < max(Printer_Queue) and Printer_Queue[pointer] != 0:

                if pointer == testcase[1]:
                    testcase[1] = len(Printer_Queue)

                pop = Printer_Queue[pointer]
                Printer_Queue.append(pop)

                if len(Printer_Queue) - 1 > testcase[1]:

                    testcase[1] -= 1

                pointer = Printer_Queue.index(max(Printer_Queue))

            Printer_Queue[pointer] = 0

        print(count)









