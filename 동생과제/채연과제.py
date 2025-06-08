import os
import datetime

# 유통기한 관리 기능
def Expriation_date():

    print('=' * 29)
    print('\t유통기한 관리')
    print('=' * 29)

    print('유통기한 빠른순 ▼\n')
    print('냉장\t냉동\t실온\n')
    print('달걀\n유통기한: D-2\n')
    print('브로콜리\n유통기한: D-5\n')
    print('닭가슴살\n유통기한: D+1\t2025.04.29')

# 레시피 추천 기능
def Recommend_recipe():

    print('=' * 27)
    print('\t레시피 추천')
    print('=' * 27, end="\n\n")

    print('브로콜리 달걀 볶음')
    print('사용재료: 달걀, 브로콜리')
    print('재료유통기한: 달걀(D-2), 브로콜리(D-5)')
    print('조리시간: 약 15분\t 난이도: 하\t 레시피보기\n')

    print('닭가슴살 달걀 샐러드')
    print('사용재료: 닭가슴살, 달걀')
    print('재료유통기한: 닭가슴살(D-1), 달걀(D-2)')
    print('조리시간: 약 10분\t 난이도: 중\t 레시피보기\n')

    print('브로콜리 수프')
    print('사용재료: 브로콜리')
    print('재료유통기한: 브로콜리(D-5)')
    print('조리시간: 약 20분\t 난이도: 중\t 레시피보기\n')

# 영수증 스캔 기능
def Print_receipt():

    print('=' * 27)
    print('\t영수증 스캔')
    print('=' * 27)
    print("\n영수증을 스캔해주세요.\n")

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 영수증 상단
    print("=" * 50)
    print("영수증".center(50))
    print("=" * 50)
    
    # 현재 시간
    print(f"날짜: {current_time}")
    print("-" * 50)
    
    # 상품 목록
    items = [
        {"name": "계란", "price": 5000, "quantity": 1},
        {"name": "브로콜리", "price": 2500, "quantity": 2},
        {"name": "닭가슴살", "price": 3000, "quantity": 10},
    ]
    
    total_price = 0

    # 각 항목의 금액 계산
    for item in items:
        
        total_item_price = item['price'] * item['quantity']
        print(f"{item['name']:<20} {item['quantity']:>5}개 {total_item_price:>10,} 원")
        total_price += total_item_price
    
    print("-" * 50)
    
    # 총합
    print(f"{'총합':<20} {total_price:>10,} 원")
    
    # 하단
    print("=" * 50)
    print("\t   감사합니다! 좋은 하루 되세요.")
    print("=" * 50)

# 메인함수
if __name__ == "__main__":
    
    # 메인화면
    print('=' * 28)
    print('\tFOOD MANAGER')
    print('=' * 28, end='\n\n')
    main = input('원하는 기능을 입력해주십시오.\n\n○ 유통기한 관리\n○ 레시피 추천\n○ 영수증 스캔\n\n')

    # 입력값이 맞게 기능 구현
    match main:

        case '유통기한 관리':
        
            os.system('clear')
            Expriation_date()

        case '레시피 추천':

            os.system('clear')
            Recommend_recipe()

        case '영수증 스캔':

            os.system('clear')
            Print_receipt()

        case default:

            print('잘못 입력하셨습니다.')

