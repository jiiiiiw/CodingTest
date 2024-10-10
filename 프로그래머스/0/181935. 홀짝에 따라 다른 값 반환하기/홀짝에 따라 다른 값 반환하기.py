def solution(n):
    answer = 0
    
    if not n % 2:
        for i in range(0,n+1,2):
            answer += i**2
    else:
        for i in range(1,n+1,2):
            answer += i
    
    return answer