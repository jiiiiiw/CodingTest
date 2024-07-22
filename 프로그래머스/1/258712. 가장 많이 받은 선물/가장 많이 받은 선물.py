def solution(friends, gifts):
    gifted = {}  # 각 친구가 누구에게 몇 번의 선물을 주었는지 저장
    gift_idx = {}  # 각 친구의 선물 지수 (받은 선물의 수 - 준 선물의 수)
    
    # 초기화
    for friend in friends:
        gifted[friend] = {}
        gift_idx[friend] = 0
    
    # 선물 기록 처리
    for gift in gifts:
        t, f = gift.split(' ')
        if f in gifted[t]:
            gifted[t][f] += 1
        else:
            gifted[t][f] = 1
        
        gift_idx[t] += 1
        gift_idx[f] -= 1
    
    # 각 친구가 몇 번의 선물을 받을 수 있는지 계산
    will_get = [0 for _ in friends]
    for i in range(len(friends)):
        curr = friends[i]
        for j in range(i + 1, len(friends)):
            another = friends[j]
            
            a = gifted[curr][another] if another in gifted[curr] else 0
            b = gifted[another][curr] if curr in gifted[another] else 0
            
            if a > b:
                will_get[i] += 1
            elif a < b:
                will_get[j] += 1
            elif a == b:
                ai, bi = gift_idx[curr], gift_idx[another]
                if ai > bi:
                    will_get[i] += 1
                elif ai < bi:
                    will_get[j] += 1
    
    answer = max(will_get)
    return answer