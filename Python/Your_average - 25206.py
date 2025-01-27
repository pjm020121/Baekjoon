# 25206 / Your_average

import sys

line = 20   # 수강과목 수
subject_result = 0      # 학점 * 과목평점
credit_result = 0       # 학점총합

for i in range(line):

    frame = sys.stdin.readline().split()
    credit = float(frame[1])    # 학점
    credit_result += credit 

    # 과목평점에 맞게 분류
    match frame[2]:

        case 'A+':
            subject = 4.5

        case 'A0':
            subject = 4.0

        case 'B+':
            subject = 3.5

        case 'B0':
            subject = 3.0

        case 'C+':
            subject = 2.5

        case 'C0':
            subject = 2.0
        
        case 'D+':
            subject = 1.5

        case 'D0':
            subject = 1.0

        case 'F':
            subject = 0

        # P과목은 예외처리
        case 'P':
            subject = 0
            credit_result -= credit
    
    # 학점 * 과목평점 / 학점총합(F나 P는 제외)
    subject_result += credit * subject

# 총점이 0점이하일 경우 예외처리
if subject_result <= 0:

    print(f"{0:.6f}")

else:

    print(f"{subject_result / credit_result:.6f}")

