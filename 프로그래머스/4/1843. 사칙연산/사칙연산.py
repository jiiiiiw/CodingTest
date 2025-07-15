def solution(a):
    n = len(a)
    memo = {}

    def dfs(l, r):
        if (l, r) in memo:
            return memo[(l, r)]

        if l == r:
            val = int(a[l])
            return (val, val) 

        max_val = float('-inf')
        min_val = float('inf')

        for i in range(l + 1, r, 2):
            l_max, l_min = dfs(l, i - 1)
            r_max, r_min = dfs(i + 1, r)

            if a[i] == '+':
                max_val = max(max_val, l_max + r_max)
                min_val = min(min_val, l_min + r_min)
            else:  # '-'
                max_val = max(max_val, l_max - r_min)
                min_val = min(min_val, l_min - r_max)

        memo[(l, r)] = (max_val, min_val)
        return memo[(l, r)]

    return dfs(0, n - 1)[0]