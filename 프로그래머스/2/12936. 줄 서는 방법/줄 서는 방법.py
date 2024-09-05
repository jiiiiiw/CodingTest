def factorial(n):
    # 팩토리얼 계산 함수
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def solution(n, k):
    # 1부터 n까지 숫자를 리스트로 만듦
    people = list(range(1, n + 1))
    result = []
    k -= 1  # k번째는 0-indexed로 변환
    
    # 남은 사람들의 수에 맞춰서 순열을 하나씩 찾아감
    for i in range(n, 0, -1):
        # (i-1)!의 값 구하기
        fact = factorial(i - 1)
        
        # 현재 자리에서 선택해야 할 사람의 인덱스를 결정
        index = k // fact
        result.append(people.pop(index))
        
        # k를 다음 자리 선택을 위해 갱신
        k %= fact
    
    return result
