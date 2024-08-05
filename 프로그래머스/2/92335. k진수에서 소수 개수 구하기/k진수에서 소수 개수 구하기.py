def get_P(num_stack):
    P = 0
    for num in reversed(num_stack):
        P = P * 10 + num
    return P

def get_Ps(n, k):
    Ps = dict() # 소수의 등장 횟수를 기록하기 위해서 dict을 사용
    num_stack = [] # k진수의 자릿수를 의미한다.
    while n:
        curr = n%k
        if curr == 0: # 문제 조건에 해당 ! 경각심 가지기 !!
            if num_stack:
                P = get_P(num_stack)
                if P in Ps:
                    Ps[P] += 1
                else:
                    Ps[P] = 1
            num_stack = []
        else:
            num_stack.append(curr)
        n = n//k
    if num_stack:
        P = get_P(num_stack)
        if P in Ps:
            Ps[P] += 1
        else:
            Ps[P] = 1
    return Ps
            
def prime(number):
    if number in [0,1]:
        return False
    else:
        div = 2
        while div * div <= number:
            if number % div == 0:
                return False
            div += 1
        return True

def solution(n, k):
    Ps = get_Ps(n,k)
    
    answer = 0
    for P in Ps.keys():
        if prime(P):
            answer += Ps[P]
    return answer