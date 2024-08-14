from collections import deque # 큐 import

def solution(queue1, queue2):
    s1 = sum(queue1)
    s2 = sum(queue2)
    
    if (s1 + s2) % 2: # 홀수이면 절대 이분할을 할 수가 없다
        return -1
    
    queue1 = deque(queue1) # list를 queue로 바꾸어주기
    queue2 = deque(queue2)
    count = 0
    limit = len(queue1) + len(queue2)
    start = 0
    
    while start < 2 * limit: # 무한 뤂에 빠질 수 있는 가능성을 배제
        if s1 == s2:
            return count
        elif s1 > s2:
            item = queue1.popleft()
            s1 -= item
            queue2.append(item)
            s2 += item
        else:
            item = queue2.popleft()
            s2 -= item
            queue1.append(item)
            s1 += item
        count += 1
        start += 1
    return -1