import math

def solution(W, H):
    # 최대 공약수 계산
    gcd_value = math.gcd(W, H)
    
    # 사용할 수 있는 정사각형 개수 계산
    return W * H - (W + H - gcd_value)
