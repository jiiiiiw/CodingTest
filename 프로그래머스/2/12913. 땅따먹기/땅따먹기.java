class Solution {
    int solution(int[][] l) {
        int n = l.length;
        
        for (int i = 1; i < n; i++) {
            l[i][0] += Math.max(l[i-1][1], Math.max(l[i-1][2], l[i-1][3]));
            l[i][1] += Math.max(l[i-1][0], Math.max(l[i-1][2], l[i-1][3]));
            l[i][2] += Math.max(l[i-1][0], Math.max(l[i-1][1], l[i-1][3]));
            l[i][3] += Math.max(l[i-1][0], Math.max(l[i-1][1], l[i-1][2]));
        }
        
        int[] last = l[n - 1];
        return Math.max(Math.max(last[0], last[1]), Math.max(last[2], last[3]));
    }
}