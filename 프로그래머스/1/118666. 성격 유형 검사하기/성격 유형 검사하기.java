import java.util.*;

public class Solution {
    public String solution(String[] s, int[] c) {
        Map<Character, Integer> m = new HashMap<>();
        m.put('R', 0);
        m.put('T', 0);
        m.put('C', 0);
        m.put('F', 0);
        m.put('J', 0);
        m.put('M', 0);
        m.put('A', 0);
        m.put('N', 0);

        for (int i = 0; i < s.length; i++) {
            char x = s[i].charAt(0); 
            char y = s[i].charAt(1); 
            int v = c[i];

            if (v < 4) {
                m.put(x, m.get(x) + (4 - v));
            } else if (v > 4) {
                m.put(y, m.get(y) + (v - 4));
            }
        }

        StringBuilder r = new StringBuilder();
        r.append(m.get('R') >= m.get('T') ? 'R' : 'T');
        r.append(m.get('C') >= m.get('F') ? 'C' : 'F');
        r.append(m.get('J') >= m.get('M') ? 'J' : 'M');
        r.append(m.get('A') >= m.get('N') ? 'A' : 'N');

        return r.toString();
    }
}
