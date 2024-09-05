from itertools import permutations

def calculate(operators, numbers, operator):
    """주어진 연산자를 처리하여 새로운 리스트로 반환"""
    while operator in operators:
        idx = operators.index(operator)
        num1 = numbers[idx]
        num2 = numbers[idx + 1]
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        numbers[idx:idx + 2] = [result]  # 결과값으로 숫자 리스트 갱신
        operators.pop(idx)  # 처리한 연산자 삭제
    return numbers, operators

def solution(expression):
    # 1. 숫자와 연산자를 분리
    import re
    numbers = list(map(int, re.split(r'[\+\-\*]', expression)))
    operators = re.findall(r'[\+\-\*]', expression)
    
    # 2. 가능한 연산자 우선순위 조합 생성
    operator_priority = list(permutations(['+', '-', '*']))
    
    max_value = 0
    
    # 3. 각 연산자 우선순위에 대해 계산
    for priority in operator_priority:
        tmp_numbers = numbers[:]
        tmp_operators = operators[:]
        
        # 각 우선순위에 따라 차례대로 연산
        for op in priority:
            tmp_numbers, tmp_operators = calculate(tmp_operators, tmp_numbers, op)
        
        # 결과값의 절댓값을 비교하여 최대값 갱신
        max_value = max(max_value, abs(tmp_numbers[0]))
    
    return max_value
