def solution(bandage, health, attacks):
    now_health = health 
    attack_time = [i[0] for i in attacks]
    dealing = [i[1] for i in attacks]
    max_time = max([i[0] for i in attacks]) 
    bandage_time = bandage[0] 
    second_healing = bandage[1] 
    more_healing = bandage[2] 
    cnt = 0
    for time in range(1,max_time+1):
        if time in attack_time: 
            cnt = 0 
            now_health -= dealing[attack_time.index(time)] 
            if now_health <= 0: 
                answer = -1
                return answer
        else:
            cnt +=1
            if cnt == bandage_time:
                cnt = 0
                now_health += more_healing
                if now_health >= health :
                    now_health = health
            if now_health == health: 
                pass
            else: 
                now_health += second_healing
                if now_health >= health:
                    now_health = health
    print(now_health)

    if now_health <= 0:
        answer = -1
    else:
        answer = now_health
    return answer