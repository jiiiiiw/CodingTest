def solution(n):
    # 단순 DP -> 시간 복잡도가 올라갈 가능성이 농후하다
    # 상태를 저장하면서 DP를 진행하자
    
    Casecount = [0 for __ in range(max(3, n+1))] # 밑에 초기화를 보장해주어야 한다.
    Casecount[0], Casecount[1], Casecount[2] = 0, 1, 2
    #Casecount[A] =  Casecount[A-1] + Casecount[A-2] 로 접근이 가능하다.
    
    for idx in range(3, n+1):
        Casecount[idx] = Casecount[idx-1] + Casecount[idx-2]
    
    return Casecount[n] % 1234567