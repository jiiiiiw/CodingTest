from itertools import combinations

def solution(relation):
    n_row = len(relation)    # 행의 개수
    n_col = len(relation[0]) # 열의 개수
    candidates = []

    # 1. 모든 가능한 컬럼 조합을 구한다
    for i in range(1, n_col + 1):
        for comb in combinations(range(n_col), i):
            # 2. 해당 조합으로 유일성 체크
            tmp = [tuple([item[c] for c in comb]) for item in relation]
            if len(set(tmp)) == n_row:  # 유일성 만족
                # 3. 최소성 체크
                if not any(set(c).issubset(set(comb)) for c in candidates):
                    candidates.append(comb)

    # 4. 후보키의 개수를 반환
    return len(candidates)
