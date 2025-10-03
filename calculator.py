"""
계산기 모듈
간단한 수학 연산을 수행하는 계산기 기능을 제공합니다.
"""

class Calculator:
    """간단한 계산기 클래스"""
    
    def __init__(self):
        """계산기 초기화"""
        self.history = []
    
    def add(self, a: float, b: float) -> float:
        """두 수를 더합니다"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """두 수를 뺍니다"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """두 수를 곱합니다"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """두 수를 나눕니다"""
        if b == 0:
            raise ValueError("0으로 나눌 수 없습니다")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self) -> list:
        """계산 기록을 반환합니다"""
        return self.history.copy()
    
    def clear_history(self):
        """계산 기록을 지웁니다"""
        self.history.clear()


if __name__ == "__main__":
    # 계산기 테스트
    calc = Calculator()
    
    print("🧮 간단한 계산기")
    print("=" * 30)
    
    # 기본 연산 테스트
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 3 = {calc.subtract(10, 3)}")
    print(f"4 * 6 = {calc.multiply(4, 6)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    
    print("\n📝 계산 기록:")
    for record in calc.get_history():
        print(f"  {record}")