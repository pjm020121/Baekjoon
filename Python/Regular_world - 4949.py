# 4949 / Regular_world
import sys

# .을 기준으로 문자열 나눠주기
string = sys.stdin.read().split('.')
del string[-2:]

# 띄어쓰기 생략
for i in range(len(string)):

    string[i] = ''.join(string[i]).replace(' ','')

# 괄호의 개수 및 순서 고려해서 맞지 않으면 break
for i in range(len(string)):
    
    cnt = 0
    tmp = 0
    last_open = list()
    vaild = True

    for k in range(len(string[i])):

        if cnt < 0 or tmp < 0:

            vaild = False
            break  

        if string[i][k] == '[':

            cnt += 1
            last_open.append('[')

        elif string[i][k] == ']':

            if len(last_open) > 0:

                if last_open[len(last_open) - 1] != '[':
                    vaild = False
                    break
                last_open.pop(len(last_open) - 1)

            cnt -= 1

        if string[i][k] == '(':

            tmp += 1
            last_open.append('(')

        elif string[i][k] == ')':
            
            if len(last_open) > 0:

                if last_open[len(last_open) - 1] != '(':
                    vaild = False
                    break

                last_open.pop(len(last_open) - 1)
            
            tmp -= 1

    # 호환성 및 개수가 맞다면 정답
    if vaild and cnt == 0 and tmp == 0:
        
        print('yes')    

    else:

        print('no')

