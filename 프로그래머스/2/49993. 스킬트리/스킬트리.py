def solution(skill, skill_trees):
    answer = 0
    arr = []
    
    for i in range(len(skill_trees)):
        check1 = 0
        check2 = 0
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                check2 += 1
            if skill_trees[i][j] == skill[check1]:
                check1 += 1
                if check1 == len(skill):
                    break # 스킬을 모두 마스터한 상태를 의미한다
        
        if check1 == check2:
            answer += 1
            
    return answer