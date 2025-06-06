from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        top = prices.popleft()
        second = 0
        
        for price in prices:
            second += 1
            if top > price:
                break
        
        answer.append(second)
        
    return answer