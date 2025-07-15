import java.util.*;

class Solution {
    public int solution(int[] p, String[] m) {
        int n = Math.min((p[0] + p[1] + p[2]) * 5, m.length);
        List<List<String>> gList = new ArrayList<>();

        for (int i = 0; i < n; i += 5) {
            List<String> g = new ArrayList<>();
            for (int j = i; j < i + 5 && j < n; j++) {
                g.add(m[j]);
            }
            gList.add(g);
        }

        gList.sort((a, b) -> score(b) - score(a));

        int ans = 0;
        int idx = 0;

        for (int t = 0; t < p[0]; t++) {
            if (idx >= gList.size()) break;
            ans += calc(gList.get(idx++), "dia");
        }
        for (int t = 0; t < p[1]; t++) {
            if (idx >= gList.size()) break;
            ans += calc(gList.get(idx++), "iron");
        }
        for (int t = 0; t < p[2]; t++) {
            if (idx >= gList.size()) break;
            ans += calc(gList.get(idx++), "stone");
        }

        return ans;
    }


    private int score(List<String> g) {
        int s = 0;
        for (String x : g) {
            if (x.equals("diamond")) s += 25;
            else if (x.equals("iron")) s += 5;
            else s += 1;
        }
        return s;
    }

    private int calc(List<String> g, String tool) {
        int s = 0;
        for (String x : g) {
            if (tool.equals("dia")) {
                s += 1;
            } else if (tool.equals("iron")) {
                if (x.equals("diamond")) s += 5;
                else s += 1;
            } else { 
                if (x.equals("diamond")) s += 25;
                else if (x.equals("iron")) s += 5;
                else s += 1;
            }
        }
        return s;
    }
}
