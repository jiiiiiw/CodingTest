import java.util.Arrays;

class Solution {
    public int solution(int[] a, int[] b) {
        Arrays.sort(a);                  
        Arrays.sort(b);                  
        int n = a.length;
        int s = 0;                       // 누적 합

        for (int i = 0; i < n; i++) {
            s += a[i] * b[n - 1 - i];  
        }

        return s;
    }
}