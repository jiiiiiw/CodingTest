def solution(nums):
    N = len(nums) / 2
    mon = set(nums)
    
    if N <= len(mon): return N
    
    return len(mon)