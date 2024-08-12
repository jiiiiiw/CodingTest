def make(numbers, current, used, results):
    if current:
        results.add(int(current))  # 숫자 조합을 만들어서 결과에 추가
    
    for i in range(len(numbers)):
        if not used[i]:
            used[i] = True
            make(numbers, current + numbers[i], used, results)
            used[i] = False

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    results = set()
    used = [False] * len(numbers)
    
    # 모든 가능한 숫자 조합을 생성
    make(numbers, "", used, results)
    
    prime_count = 0
    for num in results:
        if is_prime(num):
            prime_count += 1
    
    return prime_count
