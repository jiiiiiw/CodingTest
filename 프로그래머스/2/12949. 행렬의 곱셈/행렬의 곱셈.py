def solution(arr1, arr2):
    # 0000   00   [[00]
    # 0000 x 00 =  [00]
    # 0000   00    [00]]
    #        00   
    # R1,C1 x R2,C2 = R1,C2
    # C1 == R2 라야 한다.
    
    R1, C1 = len(arr1), len(arr1[0])
    R2, C2 = len(arr2), len(arr2[0])
    
    
    # List Comprension을 사용한 풀이
    answer = [[sum([arr1[ans_r][mulidx]*arr2[mulidx][ans_c] for mulidx in range(C1)]) 
               for ans_c in range(C2)] 
              for ans_r in range(R1)]
    
    
    """
    # append를 사용한 풀이
    answer = []
    for ans_r in range(R1):
        line = []
        for ans_c in range(C2):
            mul_val = 0
            for mul_idx in range(C1):
                mul_val += arr1[ans_r][mul_idx] * arr2[mul_idx][ans_c]
            line.append(mul_val)
        answer.append(line)
    """
    
    return answer