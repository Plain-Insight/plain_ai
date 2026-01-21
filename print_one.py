"""
숫자 1 출력 모듈
간단하게 숫자 1을 출력하는 기능을 제공합니다.
"""

def print_number_one():
    """숫자 1을 출력하는 함수"""
    print(1)
    return 1

def get_number_one():
    """숫자 1을 반환하는 함수"""
    return 1

def main():
    """메인 실행 함수"""
    print("🔢 숫자 1 출력 프로그램")
    print("=" * 25)
    
    # 숫자 1 출력
    result = print_number_one()
    
    # 추가 정보 출력
    print(f"반환값: {result}")
    print(f"타입: {type(result)}")
    print("✅ 숫자 1 출력 완료!")

if __name__ == "__main__":
    main()