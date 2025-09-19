def solution(N, number):
    if N == number:
        return 1
    
    dp = [set() for _ in range(9)]
    
    for k in range(1,9):
        dp[k].add(int(str(N) * k))
        
        for i in range(1, k):
            for a in dp[i]:
                for b in dp[k-i]:
                    dp[k].add(a + b)
                    dp[k].add(a - b)
                    dp[k].add(a * b)
                    if b != 0:
                        dp[k].add(a // b)
        
        print(f"k={k}, count={len(dp[k])}, sample={list(dp[k])[:10]}")
        
        if number in dp[k]:
            print(f"==> number {number} found at k={k}")
            return k
    
    return -1
            