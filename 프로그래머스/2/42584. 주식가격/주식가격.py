def solution(prices):
    result = [0] * len(prices)
    stack = []
    for cur in range(len(prices)):
        while stack and prices[stack[-1]] > prices[cur]:
            pas = stack.pop()
            result[pas] = cur - pas
        stack.append(cur)
    for i in stack:
        result[i] = len(prices) - i - 1
    
    return result