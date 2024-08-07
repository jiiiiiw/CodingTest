def solution(land):
    ScoreSum = [0, 0, 0, 0] # 첫번째 행 전의 임의의 0값으로 된 행이 있다고 가정
    
    for line in land:
        NewScoreSum = [0, 0, 0, 0] # 다음 행을 위한 값
        for idx in range(4):
            PrevScoreSum = ScoreSum[:idx] + ScoreSum[idx+1:] # 같은 라인 값은 빼주기
            NewScoreSum[idx] = line[idx] + max(PrevScoreSum)
        ScoreSum = NewScoreSum # 갱신해주기
    
    return max(ScoreSum)
    