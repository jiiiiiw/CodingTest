def is_valid(s):
    # 짝을 아직 찾지 못한 괄호들을 저장하는 stack
    # 나중에 저장된 괄호가 짝을 이뤄 소거되어야
    # 이전에 저장된 괄호도 짝을 찾을 수 있기 때문에
    # stack의 구조를 사용하고 있다. (LIFO)
    stack = []
    for char in s:
        # 괄호가 짝을 이루고 있다면 소거시킨다.
        # if All True return True
        # if any False return False
        if stack and stack[-1] == '[' and char == ']':
            del stack[-1]
        elif stack and stack[-1] == '{' and char == '}':
            del stack[-1]
        elif stack and stack[-1] == '(' and char == ')':
            del stack[-1]
        # 짝을 찾지 못한 경우 stack에 저장한다.
        else:
            stack.append(char)
    # 짝을 찾지 못한 괄호들이 남아있다면 invalid 즉 False
    # 모든 괄호가 짝을 찾아 소거되었다면 valid 즉 True
    return stack == []

def solution(s):
    #  0 1 2 3 4
    #  a b c d e
    # 0 1 2 3 4 5
    answer = 0
    for x in range(len(s)):
        # left = s[:x]
        # right = s[x:]
        # rotated = right + left
        if is_valid(s[x:] + s[:x]):
            answer += 1
    return answer