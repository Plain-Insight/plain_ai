"""
숫자 0 출력 모듈
간단하게 숫자 0을 출력하는 기능을 제공합니다.
"""

def print_zero():
    """숫자 0을 출력하는 함수"""
    print(0)
    return 0

def get_zero():
    """숫자 0을 반환하는 함수"""
    return 0

def is_zero(number):
    """주어진 숫자가 0인지 확인하는 함수"""
    return number == 0

def main():
    """메인 실행 함수"""
    print("🔢 숫자 0 출력 프로그램")
    print("=" * 25)
    
    # 숫자 0 출력
    result = print_zero()
    
    # 추가 정보 출력
    print(f"반환값: {result}")
    print(f"타입: {type(result)}")
    print(f"0인가? {is_zero(result)}")
    print("✅ 숫자 0 출력 완료!")

if __name__ == "__main__":
    main()