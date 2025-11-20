# 2941 / Croatia

import sys

# 샘플링
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
sample = sys.stdin.readline().strip()
cnt = 0

# 입력받은 문자열 속 크로아티아 알파벳이 있는 경우
for i in croatia:

    if i in sample:
        
        # 중복 중첩
        repeat = sample.count(i)

        # 문자열 길이가 다른 dz=만 따로 계산
        if i != 'dz=':

            cnt += repeat

        elif i == 'dz=':
            
            cnt += 2 * repeat

# dz=속 z=가 포함되어 중첩되는 경우 예외처리
z = sample.count('z=')
dz = sample.count('dz=')

if (dz and z != 0):
    
    if dz == z:
        cnt -= z

    elif dz < z:
        cnt -= dz

print(len(sample) - cnt)