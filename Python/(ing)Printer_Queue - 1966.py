import sys

Testcase_num = int(sys.stdin.readline())

for i in range(Testcase_num):

    testcase = list(map(int, sys.stdin.readline().split()))
    Printer_Queue = list(map(int, sys.stdin.readline().split()))
    pointer = 0
    count = 0

    if testcase[0] == 1:

        print(1)

    elif testcase[0] > 1:

        for k in range(testcase[0]):
            
            print(Printer_Queue, "\n", pointer, "\n", testcase[1])
            
            count += 1

            if (pointer == testcase[1] and max_val >= max(Printer_Queue)) or len(Printer_Queue) == 1:
                break
    
            if Printer_Queue[pointer] < max(Printer_Queue):
                
                max_ind = Printer_Queue.index(max(Printer_Queue))
                max_val = max(Printer_Queue)
                Printer_Queue.pop(max_ind)

                if max_ind > len(Printer_Queue) -1:
                    max_ind -= 1

                if pointer == testcase[1]:
                    testcase[1] = len(Printer_Queue) - 1

                elif pointer < testcase[1]:
                    testcase[1] -= 1

                if max_ind > pointer:
                    max_ind -= 1

                pop = Printer_Queue.pop(pointer)
                Printer_Queue.append(pop)

                pointer = max_ind
            
            else:
                max_val = Printer_Queue.pop(pointer)

                if pointer < testcase[1]:
                    testcase[1] -= 1

                if pointer > len(Printer_Queue) -1:
                    pointer -= 1
            
        print(count)









