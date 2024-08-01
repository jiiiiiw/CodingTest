def divs(num):
    DIVS = dict()
    div = 2 
    while 1 < num:
        if num % div == 0:
            if div in DIVS:
                DIVS[div] += 1
            else:
                DIVS[div] = 1
            num = num // div
            div = 2
        else:
            div += 1
    return DIVS

def solution(arr):
    LCM = dict()
    
    for num in arr:
        NUM_DIVS = divs(num)
        for div, count in NUM_DIVS.items(): # 키값과 카운트 값을 동시에 알 수 있다.
            if div in LCM:
                LCM[div] = max(LCM[div], count)
            else:
                LCM[div] = count
    answer = 1
    for div, count in LCM.items():
        answer *= div ** count
    return answer
        
    # n1 * n2 // gcd(n1, n2)
    # n1 인수분해, n2 인수분해 각 숫자의 최대등장횟수
    
    
    