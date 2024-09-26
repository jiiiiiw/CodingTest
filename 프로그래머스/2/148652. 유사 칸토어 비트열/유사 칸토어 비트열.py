def solution(n, l, r):
    def count_ones(n, start, end):
        if n == 0:
            return 1
        
        unit_len = 5 ** (n - 1)
        unit_count = 4 ** (n - 1)
        
        quotient_s, remainder_s = divmod(start - 1, unit_len)
        quotient_e, remainder_e = divmod(end - 1, unit_len)
        
        if quotient_s == quotient_e:
            if quotient_s == 2:
                return 0
            return count_ones(n - 1, remainder_s + 1, remainder_e + 1)
        
        result = 0
        if quotient_s != 2:
            result += count_ones(n - 1, remainder_s + 1, unit_len)
        if quotient_e != 2:
            result += count_ones(n - 1, 1, remainder_e + 1)
        
        for i in range(quotient_s + 1, quotient_e):
            if i != 2:
                result += unit_count
        
        return result

    return count_ones(n, l, r)