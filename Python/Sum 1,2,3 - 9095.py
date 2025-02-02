# 9095 / Sum 1, 2, 3

import sys

# 재귀로 구현한 DP
def DP(num, mem = {}):

    if num in mem:

        return mem[num]
    
    if num == 1:

        return 1
    
    elif num == 2:
        
        return 2
    
    elif num == 3:
        
        return 4
    
    mem[num] = DP(num - 1, mem) + DP(num - 2, mem) + DP(num - 3, mem)
    return mem[num]

# 메인함수
if __name__ == "__main__":

    count = int(sys.stdin.readline())
    result = list()

    for i in range(count):

        mem = (int(sys.stdin.readline()))
        result.append(DP(mem))

    for i in result:

        print(i)


        
        
        
