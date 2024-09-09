def collatz_sequence(k):
    sequence = [k]
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = 3 * k + 1
        sequence.append(k)
    return sequence

def integrate_sequence(sequence, a, b):
    # 범위가 유효하지 않으면 -1 반환
    if a >= len(sequence) or len(sequence) + b - 1 < a:
        return -1
    
    # 실제 종료 인덱스 계산
    end = min(len(sequence) - 1, len(sequence) + b - 1)
    
    # 사다리꼴 면적 계산
    total_area = 0.0
    for i in range(a, end):
        total_area += 0.5 * (sequence[i] + sequence[i + 1])
    
    return total_area

def solution(k, ranges):
    # 1. 콜라츠 수열 생성
    sequence = collatz_sequence(k)
    
    # 2. 주어진 구간에 대해 정적분 수행
    result = []
    for a, b in ranges:
        # b가 음수이므로 실제 구간 계산은 len(sequence) + b로 처리
        area = integrate_sequence(sequence, a, b)
        result.append(area)
    
    return result
