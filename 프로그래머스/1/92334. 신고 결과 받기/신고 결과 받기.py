def solution(id_list, report, k):
    # 유저가 누구에 의해서 신고당했는지를 정리하는 부분
    reported_by = {id:set() for id in id_list} # set로 해두면 중복 방지가 편하다
    
    for rep in report:
        u, r = rep.split() # 나눈 결과를 u와 r 두 변수에 언패킹한다.
        reported_by[r].add(u)
    
    # print(reported_by)
    
    # 유저가 한 신고가 메일을 보내게되는 임계값을 넘었는지를 정리하여 성공했는지를 정리
    success = {id:0 for id in id_list}
    for id in id_list:
        if k <= len(reported_by[id]):
            for mail in reported_by[id]:
                success[mail] += 1
    
    # print(success)
    
    return [success[id] for id in id_list]
        