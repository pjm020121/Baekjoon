# 1259 / Palindrome(Number)

answer = None    # 최종값

while True:

    Palin = input()    # 입력값받기

    # 0 입력시 탈출
    if Palin == '0':
        break

    # 글자수가 홀수인경우
    if len(Palin) % 2 == 1:

        mid = len(Palin) // 2

        for i in range(len(Palin) // 2):

            if Palin[i] == Palin[len(Palin) - (i + 1)]:

                if (i + 1) == mid:
                    answer = "yes"

            else:

                answer = "no"
                break

    # 글자수가 짝수인경우
    if len(Palin) % 2 == 0:

        for i in range(len(Palin) // 2):

            if Palin[i] != Palin[len(Palin) - (i + 1)]:

                answer = "no"
                break

            else:
                answer = "yes"

    if len(Palin) == 1:
        answer = "yes"

    print(answer)