def solution(A,B):
    answer = 0
    for a, b, in zip(sorted(A, reverse = True), sorted(B)): # A는 큰 수부터 B는 작은 수부터
        answer += a * b
    return answer