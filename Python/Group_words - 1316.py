# 1316 / Group_words

import sys

count = int(input())
cnt = 0

# 그룹단어 입력받기
for i in range(count):

    group = sys.stdin.readline().split()
    cnt += 1

    # 예외처리
    if len(group[0]) <= 1:

        continue

    # 연속되는 글자가 끊길경우 같은 단어가 나오면 그룹단어 탈락
    else:
        
        for k in range(len(group[0]) - 1):

            if group[0][k] != group[0][k + 1]:
                
                if group[0][k] in group[0][k + 1:]:
                    
                    cnt -= 1
                    break
        
print(cnt)


