def solution(N, stages): # 실패율 O(n)
    answer = []
    sum_list=[0]*(N+2)
    dic_list={}
    stages.sort()
    now=len(stages)
    for i in stages:
        sum_list[i]+=1
        

    for i in range(1, N+1):
        if now==0:
            dic_list[i] = 0
            continue
        dic_list[i] = sum_list[i]/now
        now-=sum_list[i]
        
    return sorted(dic_list, key=lambda x : dic_list[x], reverse=True)