# 2747 / Fibo

import sys

# 피보나치 함수
def Fibo(n):

    result = 0
    a, b = 0, 1

    if n == 0:

        return 0
    
    elif n == 1:

        return 1
    
    for i in range(2, n + 1):

        result = a + b
        a = b
        b = result

    return result

if __name__ == '__main__':

    print(Fibo(int(sys.stdin.readline())))
    
