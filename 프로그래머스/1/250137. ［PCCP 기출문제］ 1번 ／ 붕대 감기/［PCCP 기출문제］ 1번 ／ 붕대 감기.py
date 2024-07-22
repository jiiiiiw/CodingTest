def solution(bandage, health, attacks):
    now_health = health  # 초기 체력 설정
    attack_time = [i[0] for i in attacks]  # 공격 발생 시간 리스트
    dealing = [i[1] for i in attacks]  # 각 공격의 데미지 리스트
    max_time = max([i[0] for i in attacks])  # 가장 늦게 발생하는 공격 시간
    bandage_time = bandage[0]  # 밴드 사용 시간 간격
    second_healing = bandage[1]  # 매 초당 치유량
    more_healing = bandage[2]  # 추가 치유량
    cnt = 0  # 밴드 사용 시간 간격을 추적하는 카운터
    
    for time in range(1, max_time + 1):  # 1초부터 max_time까지의 시간 루프
        if time in attack_time:  # 현재 시간이 공격 시간인 경우
            cnt = 0  # 카운터 리셋
            now_health -= dealing[attack_time.index(time)]  # 데미지 적용
            if now_health <= 0:  # 체력이 0 이하인 경우
                answer = -1
                return answer  # 캐릭터 사망, -1 반환
        else:  # 현재 시간이 공격 시간이 아닌 경우
            cnt += 1
            if cnt == bandage_time:  # 밴드 사용 시간 간격이 된 경우
                cnt = 0
                now_health += more_healing  # 추가 치유 적용
                if now_health >= health:  # 최대 체력을 초과하지 않도록 조정
                    now_health = health
            if now_health != health:  # 현재 체력이 최대 체력이 아닌 경우
                now_health += second_healing  # 매 초당 치유량 적용
                if now_health >= health:  # 최대 체력을 초과하지 않도록 조정
                    now_health = health
    
    if now_health <= 0:
        answer = -1
    else:
        answer = now_health
    return answer  # 최종 체력 반환