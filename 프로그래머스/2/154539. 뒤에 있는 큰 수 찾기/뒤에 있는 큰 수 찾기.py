def solution(numbers):
    n = len(numbers)
    answer = [-1]*n
    stack = []

    for i,number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            answer[stack.pop()] = number
        stack.append(i)

    return answer