# 한사람은 모두 나누기, 다른 사람은 하나도 나누기가 안되는 숫자를 찾는 문제
# 존재하지 않는다면 0을 반환
def divs(num):
    divs = set()
    div = 1
    while div * div <= num:
        if num % div == 0:
            divs.add(div)
            divs.add(num // div)
        div += 1
    return divs # 약수들을 set의 형태로 돌려준다

def solution(arrayA, arrayB):
    A_divs, B_divs = divs(arrayA[0]), divs(arrayB[0])
    
    for numA, numB in zip(arrayA, arrayB):
        new_A_div = set() 
        for div in A_divs:
            if numB % div and numA % div == 0:
                new_A_div.add(div)
        new_B_div = set() 
        for div in B_divs:
            if numA % div and numB % div == 0:
                new_B_div.add(div)
                
        A_divs, B_divs = new_A_div, new_B_div
        
    answer = [0] + list(A_divs) + list(B_divs)
        
    print(answer)
        
    return max(answer)