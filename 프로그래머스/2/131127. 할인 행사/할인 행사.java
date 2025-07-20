import java.util.*;

class Solution {
    public int solution(String[] w, int[] n, String[] d) {
        Map<String, Integer> m = new HashMap<>();
        for (int i = 0; i < w.length; i++) {
            m.put(w[i], n[i]); 
        }

        int c = 0; 

        for (int i = 0; i <= d.length - 10; i++) {
            Map<String, Integer> t = new HashMap<>();

            for (int j = i; j < i + 10; j++) {
                t.put(d[j], t.getOrDefault(d[j], 0) + 1);  
            }

            boolean ok = true;
            for (String k : m.keySet()) {
                if (t.getOrDefault(k, 0) < m.get(k)) {
                    ok = false;
                    break;
                }
            }

            if (ok) c++;
        }

        return c;
    }
}