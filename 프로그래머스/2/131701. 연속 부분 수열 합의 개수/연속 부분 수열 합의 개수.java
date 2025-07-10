import java.util.*;

class Solution {
    public int solution(int[] e) {
        int n = e.length;
        int[] d = new int[n * 2];

        for (int i = 0; i < n * 2; i++) {
            d[i] = e[i % n];
        }

        Set<Integer> s = new HashSet<>();

        for (int l = 1; l <= n; l++) {
            int sum = 0;
            for (int i = 0; i < l; i++) {
                sum += d[i];
            }
            s.add(sum);

            for (int i = l; i < n + l - 1; i++) {
                sum = sum - d[i - l] + d[i];
                s.add(sum);
            }
        }

        return s.size();
    }
}