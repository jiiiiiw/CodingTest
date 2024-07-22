def solution(today, terms, privacies):
    ty, tm, td = map(int, today.split("."))
    # print(ty, tm, td)
    today = ty * (12 * 28) + tm * 28 + td # 현재시점을 day 단위로 변환
    
    t2m = {tm.split()[0]:int(tm.split()[1]) for tm in terms}
    
    answer = []
    
    # print(t2m)
    for idx, privacy in enumerate(privacies): # 인덱스와 값에 대한 튜플을 생성
        start, term = privacy.split()
        # print(start,term)
        sy, sm, sd = map(int, start.split("."))
        sday = sy * (12 * 28) + sm * 28 + sd # 현재시점을 day 단위로 변환
        tmday = t2m[term] * 28
        if not today < sday + tmday: # 참이 안전한 날, 거짓이 result로
            answer.append(idx+1)        
    return answer