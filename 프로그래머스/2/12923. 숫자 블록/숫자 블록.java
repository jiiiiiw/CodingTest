import java.util.*;

class Solution {
    private static final int LIMIT = 10_000_000;

    public int[] solution(long begin, long end) {
        int n = (int) (end - begin + 1);
        int[] ans = new int[n];

        for (int i = 0; i < n; i++) {
            long x = begin + i;
            ans[i] = blockNumber(x);
        }
        return ans;
    }

    private int blockNumber(long x) {
        if (x == 1) return 0; 

        int best = 1;
        long root = (long) Math.sqrt(x);

        for (long a = 2; a <= root; a++) {
            if (x % a != 0) continue;

            long b = x / a; 
            if (b <= LIMIT) return (int) b;

            if (a <= LIMIT) best = Math.max(best, (int) a);
        }

        return best;
    }
}