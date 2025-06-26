import java.util.*;

class Solution {
    public int solution(int k, int[] t) {
        Map<Integer, Integer> m = new HashMap<>();
        for (int x : t) {
            m.put(x, m.getOrDefault(x, 0) + 1);
        }

        List<Integer> f = new ArrayList<>(m.values());
        f.sort(Collections.reverseOrder());

        int s = 0; 
        int c = 0; 

        for (int v : f) {
            s += v;
            c++;
            if (s >= k) break;
        }

        return c;
    }
}