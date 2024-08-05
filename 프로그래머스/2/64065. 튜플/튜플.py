def solution(s):
    s = s.strip('{}') # 양쪽 끝에의 해당 기호를 제거
    
    answer = []
    for elms in sorted(s.split('},{'), key = lambda x : len(x)): # 길이에 따른 정렬 완료
        for elm in map(int, elms.split(',')):
            if elm not in answer:
                answer.append(elm)
                break
                
    return answer