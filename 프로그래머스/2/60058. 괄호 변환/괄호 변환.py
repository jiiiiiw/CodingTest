def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환
    if not p:
        return ""
    
    # 2. 문자열을 두 "균형잡힌 괄호 문자열" u, v로 분리
    def split_balanced_string(s):
        balance = 0
        for i in range(len(s)):
            if s[i] == '(':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                return s[:i+1], s[i+1:]
    
    # 3. 문자열이 "올바른 괄호 문자열"인지 확인
    def is_correct(u):
        stack = []
        for char in u:
            if char == '(':
                stack.append(char)
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        return not stack
    
    # 재귀 함수 정의
    def recursive(w):
        if not w:
            return ""
        
        u, v = split_balanced_string(w)
        
        if is_correct(u):
            return u + recursive(v)
        else:
            result = "(" + recursive(v) + ")"
            # u의 첫 번째와 마지막 문자 제거, 나머지 괄호 방향을 뒤집기
            u = u[1:-1]
            reversed_u = ''.join('(' if char == ')' else ')' for char in u)
            return result + reversed_u
    
    return recursive(p)