def solution(number, k):
    answer = ''
    
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    
    if k != 0: # 탈출했는데 다담기는 경우는 예외처리가 필요하다 뒤따라온 숫자는 제거
        stack = stack[:-k]
        
    answer = ''.join(stack)
        
    return answer