def solution(str1, str2):
    answer = 0
    # 자카드 유사도 = 교집합 / 합집합
    # 단, A 와 B가 모두 공집합이면 유사도는 1이 된다
    
    # 1. 문자열 2글자씩 끊기
    set1, set2 = [], []
    for i in range(len(str1)-1):
        str_temp = str1[i] + str1[i+1]
        if str_temp.isalpha():
            set1.append(str_temp.upper())
    for j in range(len(str2)-1):
        str_temp = str2[j] + str2[j+1]
        if str_temp.isalpha():
            set2.append(str_temp.upper())
            
    # 2. 교 합 구하기
    count_times = 0
    set_temp = set2.copy()
    for k in set1:
        if k in set_temp:
            count_times += 1
            set_temp.remove(k)
    
    count_sum = len(set1) + len(set2) - count_times
    
    # 3. 자카드 유사도 계산
    if count_sum == 0:
        answer = 1*65536
    else:
        answer = int(count_times*65536/count_sum)
    
    return answer